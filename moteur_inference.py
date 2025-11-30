#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur d'Inference - Systeme Expert Prix PC Portable
=====================================================

Ce module contient la classe MoteurInference qui implemente :
- Le chainage avant (forward chaining) pour l'evaluation des regles
- La verification des conditions (requises, optionnelles, excluantes)
- Le calcul des scores de confiance
- Le tri et la selection des meilleures estimations

Le moteur d'inference est le coeur du systeme expert. Il utilise
les faits collectes (base de faits) pour evaluer les regles (base de regles)
et determiner les estimations de prix les plus probables.
"""

from typing import List, Dict, Tuple, Any


class MoteurInference:
    """
    Classe implementant le moteur d'inference en chainage avant.
    
    Le moteur d'inference evalue les regles de la base de regles
    en fonction des faits de la base de faits pour produire
    des estimations de prix avec leur niveau de confiance.
    
    Attributes:
        base_faits: Instance de la classe BaseFaits
        base_regles: Instance de la classe BaseRegles
        seuil_confiance (float): Seuil minimum de confiance pour retenir une estimation
    """
    
    def __init__(self, base_faits, base_regles, seuil_confiance: float = 0.4):
        """
        Initialise le moteur d'inference.
        
        Args:
            base_faits: Instance de BaseFaits contenant les specifications
            base_regles: Instance de BaseRegles contenant les regles
            seuil_confiance: Seuil minimum de confiance (defaut: 0.4)
        """
        self.base_faits = base_faits
        self.base_regles = base_regles
        self.seuil_confiance = seuil_confiance
    
    def verifier_condition(self, cle: str, valeurs_acceptees: Any) -> bool:
        """
        Verifie si un fait correspond aux valeurs acceptees par une condition.
        
        Args:
            cle: La cle du fait a verifier
            valeurs_acceptees: Liste de valeurs acceptees ou valeur booleenne
            
        Returns:
            True si la condition est satisfaite, False sinon
        """
        valeur_utilisateur = self.base_faits.obtenir_fait(cle)
        
        if valeur_utilisateur is None:
            return False
        
        # Si c'est une liste de valeurs acceptees
        if isinstance(valeurs_acceptees, list):
            return valeur_utilisateur in valeurs_acceptees
        # Si c'est une valeur booleenne
        elif isinstance(valeurs_acceptees, bool):
            return valeur_utilisateur == valeurs_acceptees
        else:
            return valeur_utilisateur == valeurs_acceptees
    
    def verifier_conditions_excluantes(self, regle: Dict) -> bool:
        """
        Verifie si des conditions excluantes sont presentes.
        
        Args:
            regle: La regle a evaluer
            
        Returns:
            True si une condition excluante est satisfaite (regle exclue), False sinon
        """
        conditions_excluantes = regle.get("conditions_excluantes", {})
        
        for cle, valeurs in conditions_excluantes.items():
            if self.verifier_condition(cle, valeurs):
                return True  # Une condition excluante est satisfaite
        
        return False  # Aucune condition excluante satisfaite
    
    def calculer_ratio_conditions_requises(self, regle: Dict) -> float:
        """
        Calcule le ratio de conditions requises satisfaites.
        
        Args:
            regle: La regle a evaluer
            
        Returns:
            Ratio entre 0 et 1 des conditions requises satisfaites
        """
        conditions_requises = regle.get("conditions_requises", {})
        
        if not conditions_requises:
            return 1.0  # Pas de conditions requises = toutes satisfaites
        
        conditions_satisfaites = 0
        total_conditions = len(conditions_requises)
        
        for cle, valeurs in conditions_requises.items():
            if self.verifier_condition(cle, valeurs):
                conditions_satisfaites += 1
        
        return conditions_satisfaites / total_conditions
    
    def calculer_bonus_optionnels(self, regle: Dict) -> float:
        """
        Calcule le bonus de confiance pour les conditions optionnelles satisfaites.
        
        Args:
            regle: La regle a evaluer
            
        Returns:
            Bonus de confiance (entre 0 et 0.15)
        """
        conditions_optionnelles = regle.get("conditions_optionnelles", {})
        
        if not conditions_optionnelles:
            return 0.0
        
        nb_satisfaites = 0
        total_optionnelles = len(conditions_optionnelles)
        
        for cle, valeurs in conditions_optionnelles.items():
            if self.verifier_condition(cle, valeurs):
                nb_satisfaites += 1
        
        # Bonus maximum de 15%
        bonus = (nb_satisfaites / total_optionnelles) * 0.15
        return bonus
    
    def evaluer_regle(self, regle: Dict) -> Tuple[bool, float]:
        """
        Evalue une regle par rapport aux faits de l'utilisateur.
        
        Cette methode implemente la logique principale du chainage avant :
        1. Verifier les conditions excluantes (si une est vraie -> rejeter)
        2. Verifier les conditions requises (au moins 50% doivent etre vraies)
        3. Calculer le score de confiance avec bonus optionnels
        
        Args:
            regle: La regle a evaluer
            
        Returns:
            Tuple (correspondance, score_confiance)
            - correspondance: True si la regle s'applique
            - score_confiance: Score de confiance ajuste (0 a 1)
        """
        # Etape 1 : Verifier les conditions excluantes
        if self.verifier_conditions_excluantes(regle):
            return (False, 0.0)
        
        # Etape 2 : Verifier les conditions requises
        ratio_requis = self.calculer_ratio_conditions_requises(regle)
        
        # Si moins de 50% des conditions requises sont satisfaites, rejeter
        if ratio_requis < 0.5:
            return (False, 0.0)
        
        # Etape 3 : Calculer le score de confiance
        confiance = regle["confiance_base"]
        
        # Ajuster selon le ratio de conditions requises satisfaites
        # (70% de base + 30% proportionnel au ratio)
        confiance *= (0.7 + 0.3 * ratio_requis)
        
        # Etape 4 : Ajouter le bonus pour les conditions optionnelles
        bonus = self.calculer_bonus_optionnels(regle)
        confiance = min(1.0, confiance + bonus)
        
        return (True, confiance)
    
    def inferer(self) -> List[Tuple[str, float, str, int, int]]:
        """
        Execute le moteur d'inference en chainage avant.
        
        Evalue toutes les regles de la base de regles en fonction
        des faits collectes et retourne les estimations de prix
        triees par ordre de confiance decroissante.
        
        Returns:
            Liste de tuples (nom_gamme, score_confiance, description, prix_min, prix_max)
        """
        estimations = []
        gammes_vues = set()  # Pour eviter les doublons
        
        # Evaluer chaque regle de la base de regles
        for regle in self.base_regles.obtenir_regles():
            correspond, confiance = self.evaluer_regle(regle)
            
            # Garder seulement les estimations au-dessus du seuil de confiance
            if correspond and confiance > self.seuil_confiance:
                cle_gamme = regle["nom"]
                
                # Garder seulement la meilleure confiance pour chaque gamme
                if cle_gamme not in gammes_vues:
                    gammes_vues.add(cle_gamme)
                    estimations.append((
                        regle["nom"],
                        confiance,
                        regle["description"],
                        regle["prix_min"],
                        regle["prix_max"]
                    ))
                else:
                    # Mettre a jour si meilleure confiance
                    for i, (nom, conf, desc, pmin, pmax) in enumerate(estimations):
                        if nom == cle_gamme and confiance > conf:
                            estimations[i] = (
                                regle["nom"],
                                confiance,
                                regle["description"],
                                regle["prix_min"],
                                regle["prix_max"]
                            )
                            break
        
        # Trier par confiance decroissante
        estimations.sort(key=lambda x: x[1], reverse=True)
        
        return estimations
    
    def afficher_resultats(self, estimations: List[Tuple[str, float, str, int, int]],
                           max_resultats: int = 3) -> None:
        """
        Affiche les resultats de l'inference de maniere formatee.
        
        Args:
            estimations: Liste des estimations retournees par inferer()
            max_resultats: Nombre maximum de resultats a afficher (defaut: 3)
        """
        print("\n" + "=" * 65)
        print("    RESULTATS DE L'ESTIMATION")
        print("=" * 65)
        
        if not estimations:
            print("\n[?] Aucune estimation ne correspond aux specifications fournies.")
            print("    Cela peut signifier :")
            print("    - Les specifications sont inhabituelles")
            print("    - La combinaison de composants est atypique")
            print("    - Il manque des donnees dans notre base de regles")
            print("\n    Consultez les sites marchands pour une estimation directe.")
        else:
            nb_resultats = min(max_resultats, len(estimations))
            print(f"\n[>] {nb_resultats} estimation(s) possible(s) :\n")
            
            for i, (nom, confiance, description, prix_min, prix_max) in enumerate(estimations[:nb_resultats], 1):
                pourcentage = confiance * 100
                
                # Indicateur de confiance
                if pourcentage >= 80:
                    indicateur = "[***] Forte probabilite"
                elif pourcentage >= 60:
                    indicateur = "[**]  Probabilite moyenne"
                else:
                    indicateur = "[*]   Faible probabilite"
                
                # Formatage du prix
                if prix_max >= 10000:
                    prix_str = f"> {prix_min} euros"
                else:
                    prix_str = f"{prix_min} - {prix_max} euros"
                
                print(f"  {i}. {nom}")
                print(f"     Fourchette de prix : {prix_str}")
                print(f"     Confiance : {pourcentage:.1f}% - {indicateur}")
                print(f"     Description : {description}")
                print()
        
        # Rappel de l'avertissement
        print("-" * 65)
        print("RAPPEL : Cette estimation est INDICATIVE uniquement.")
        print("Les prix reels peuvent varier significativement.")
        print("Consultez plusieurs revendeurs pour comparer les offres.")
        print("=" * 65)
    
    def obtenir_meilleure_estimation(self) -> Tuple[str, float, str, int, int]:
        """
        Retourne la meilleure estimation (celle avec la confiance la plus elevee).
        
        Returns:
            Tuple (nom_gamme, score_confiance, description, prix_min, prix_max)
            ou None si aucune estimation
        """
        estimations = self.inferer()
        
        if estimations:
            return estimations[0]
        return None
    
    def modifier_seuil_confiance(self, nouveau_seuil: float) -> None:
        """
        Modifie le seuil minimum de confiance pour les estimations.
        
        Args:
            nouveau_seuil: Nouveau seuil entre 0 et 1
        """
        if 0 <= nouveau_seuil <= 1:
            self.seuil_confiance = nouveau_seuil
            print(f"[OK] Seuil de confiance modifie a {nouveau_seuil * 100:.0f}%")
        else:
            print("[!] Le seuil doit etre entre 0 et 1.")
