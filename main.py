#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Systeme Expert - Estimation du Prix d'un Ordinateur Portable
=============================================================

Point d'entree principal du systeme expert.

Auteur: TP Universitaire - Intelligence Artificielle
Date: Novembre 2025

Description:
    Ce programme implemente un systeme expert utilisant le chainage avant
    (forward chaining) pour estimer la gamme de prix d'un ordinateur portable
    a partir de ses specifications techniques renseignees par l'utilisateur.

Structure du projet:
    - main.py           : Point d'entree et orchestration
    - base_faits.py     : Gestion des faits (specifications utilisateur)
    - base_regles.py    : Gestion des regles d'estimation
    - moteur_inference.py : Moteur d'inference en chainage avant

Gammes de prix estimees:
    1. Entree de gamme (< 500 euros)
    2. Petit budget (500 - 799 euros)
    3. Bon rapport qualite/prix (800 - 1 199 euros)
    4. Milieu/haut de gamme (1 200 - 1 799 euros)
    5. Haut de gamme / Createur (1 800 - 2 499 euros)
    6. Premium / Workstation (> 2 500 euros)

AVERTISSEMENT:
    Ce systeme est UNIQUEMENT a but educatif et pedagogique.
    Les estimations de prix sont INDICATIVES et peuvent varier selon
    le marche, les promotions et la disponibilite des produits.

Exemple d'execution:
    $ python main.py
    
    === SYSTEME EXPERT - ESTIMATION PRIX PC PORTABLE ===
    
    Repondez aux questions pour obtenir une estimation de prix.
    
    Quelle est la taille de l'ecran ?
    1. 14 pouces
    2. 15.6 pouces
    ...
    
    === ESTIMATION DE PRIX ===
    1. Milieu/haut de gamme (1 200 - 1 799 euros) - Confiance: 85%
    2. Bon rapport qualite/prix (800 - 1 199 euros) - Confiance: 65%
"""

# Importation des modules du systeme expert
from base_faits import BaseFaits
from base_regles import BaseRegles
from moteur_inference import MoteurInference


class SystemeExpertPrixPC:
    """
    Classe principale orchestrant le systeme expert.
    
    Cette classe coordonne les trois composants principaux :
    - La base de faits (specifications du PC)
    - La base de regles (regles d'estimation)
    - Le moteur d'inference (chainage avant)
    
    Attributes:
        base_faits (BaseFaits): Instance de la base de faits
        base_regles (BaseRegles): Instance de la base de regles
        moteur (MoteurInference): Instance du moteur d'inference
    """
    
    def __init__(self):
        """Initialise le systeme expert avec ses trois composants."""
        # Initialisation des composants
        self.base_faits = BaseFaits()
        self.base_regles = BaseRegles()
        self.moteur = MoteurInference(self.base_faits, self.base_regles)
    
    def afficher_avertissement(self) -> None:
        """Affiche l'avertissement obligatoire sur le caractere indicatif des estimations."""
        print("\n" + "=" * 65)
        print("    AVERTISSEMENT IMPORTANT")
        print("=" * 65)
        print("Ce systeme expert est UNIQUEMENT a but EDUCATIF.")
        print("Les estimations de prix sont INDICATIVES et peuvent varier selon :")
        print("  - Les promotions et offres en cours")
        print("  - La disponibilite des produits")
        print("  - Le marche et la region d'achat")
        print("  - Les configurations exactes des modeles")
        print("Consultez les sites marchands pour des prix reels.")
        print("=" * 65 + "\n")
    
    def afficher_entete(self) -> None:
        """Affiche l'en-tete du programme."""
        print("\n" + "=" * 65)
        print("    SYSTEME EXPERT - ESTIMATION PRIX PC PORTABLE")
        print("    Estimation de la gamme de prix selon les specifications")
        print("=" * 65)
    
    def executer(self) -> None:
        """
        Point d'entree principal du systeme expert.
        
        Execute le cycle complet du chainage avant :
        1. Affichage de l'en-tete et de l'avertissement
        2. Collecte des faits (specifications du PC)
        3. Affichage du resume des faits
        4. Inference (evaluation des regles)
        5. Affichage des resultats
        """
        # Etape 1 : Affichage de l'en-tete
        self.afficher_entete()
        
        # Etape 2 : Avertissement
        self.afficher_avertissement()
        
        # Demander confirmation pour continuer
        input("Appuyez sur Entree pour commencer le questionnaire...")
        
        # Etape 3 : Collecte des faits (chainage avant - phase de collecte)
        self.base_faits.collecter_faits()
        
        # Etape 4 : Afficher le resume des faits collectes
        self.base_faits.afficher_resume()
        
        # Etape 5 : Inference (chainage avant - phase d'evaluation)
        estimations = self.moteur.inferer()
        
        # Etape 6 : Affichage des resultats
        self.moteur.afficher_resultats(estimations)
        
        # Message de fin
        print("\nMerci d'avoir utilise le systeme expert d'estimation de prix !\n")
    
    def ajouter_regle(self, nom: str, prix_min: int, prix_max: int,
                      description: str, conditions_requises: dict,
                      conditions_optionnelles: dict = None,
                      conditions_excluantes: dict = None,
                      confiance_base: float = 0.75) -> None:
        """
        Raccourci pour ajouter une regle a la base de regles.
        
        Args:
            nom: Nom de la gamme de prix
            prix_min: Prix minimum de la fourchette
            prix_max: Prix maximum de la fourchette
            description: Description de la gamme
            conditions_requises: Dict des conditions obligatoires
            conditions_optionnelles: Dict des conditions bonus
            conditions_excluantes: Dict des conditions excluantes
            confiance_base: Niveau de confiance de base (0 a 1)
        """
        self.base_regles.ajouter_regle(
            nom, prix_min, prix_max, description,
            conditions_requises, conditions_optionnelles,
            conditions_excluantes, confiance_base
        )
    
    def afficher_regles(self) -> None:
        """Affiche toutes les regles de la base de regles."""
        self.base_regles.afficher_regles()
    
    def reinitialiser(self) -> None:
        """Reinitialise la base de faits pour une nouvelle estimation."""
        self.base_faits.reinitialiser()
        print("[OK] Base de faits reinitialisee.")


def afficher_menu() -> str:
    """
    Affiche le menu principal et retourne le choix de l'utilisateur.
    
    Returns:
        Le choix de l'utilisateur
    """
    print("\n" + "-" * 40)
    print("    MENU PRINCIPAL")
    print("-" * 40)
    print("  1. Lancer une estimation de prix")
    print("  2. Afficher les regles du systeme")
    print("  3. Quitter")
    print("-" * 40)
    
    return input("Votre choix (1-3) : ").strip()


def main():
    """
    Fonction principale du programme.
    
    Propose un menu permettant de :
    - Lancer une estimation de prix
    - Afficher les regles du systeme
    - Quitter le programme
    """
    # Creation du systeme expert
    systeme = SystemeExpertPrixPC()
    
    print("\n" + "=" * 65)
    print("    BIENVENUE DANS LE SYSTEME EXPERT PRIX PC PORTABLE")
    print("=" * 65)
    
    while True:
        choix = afficher_menu()
        
        if choix == "1":
            # Reinitialiser avant une nouvelle estimation
            systeme.reinitialiser()
            # Lancer l'estimation
            systeme.executer()
        
        elif choix == "2":
            # Afficher les regles
            systeme.afficher_regles()
        
        elif choix == "3":
            print("\nAu revoir !\n")
            break
        
        else:
            print("[!] Choix invalide. Veuillez entrer 1, 2 ou 3.")


# ============================================================
# POINT D'ENTREE DU PROGRAMME
# ============================================================

if __name__ == "__main__":
    main()
