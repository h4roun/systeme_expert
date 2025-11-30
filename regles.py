#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur d'Inférence avec Experta - Système Expert Prix PC Portable
==================================================================

Ce module implémente le KnowledgeEngine d'Experta avec toutes les règles
d'estimation de prix pour un PC portable.

Experta utilise l'algorithme RETE pour le pattern matching, ce qui est
plus efficace que notre implémentation manuelle précédente.

Classes:
    - SystemeExpertPrixPC: KnowledgeEngine principal avec les règles

Usage:
    >>> from regles import SystemeExpertPrixPC
    >>> from faits import SpecificationPC
    >>>
    >>> engine = SystemeExpertPrixPC()
    >>> engine.reset()
    >>> engine.declare(SpecificationPC(
    ...     processeur="Intel Core i7",
    ...     ram="16 Go",
    ...     carte_graphique="NVIDIA RTX 4060"
    ... ))
    >>> engine.run()
    >>> estimations = engine.obtenir_estimations()
"""

from experta import *
from faits import SpecificationPC, Estimation, GammeExclue


class SystemeExpertPrixPC(KnowledgeEngine):
    """
    Moteur d'inférence Experta pour l'estimation de prix PC.
    
    Ce KnowledgeEngine contient toutes les règles d'estimation
    de prix basées sur les spécifications du PC.
    
    L'algorithme RETE d'Experta permet un pattern matching
    efficace sur les faits déclarés.
    
    Attributes:
        estimations (list): Liste des estimations générées
    """
    
    def __init__(self):
        """Initialise le moteur d'inférence."""
        super().__init__()
        self.estimations = []
    
    # ============================================================
    # FAIT INITIAL
    # ============================================================
    
    @DefFacts()
    def faits_initiaux(self):
        """Déclare les faits initiaux au démarrage."""
        yield Fact(systeme="actif")
    
    # ============================================================
    # REGLES D'EXCLUSION (s'exécutent en premier avec salience élevée)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in [
                "Intel Core i7", "Intel Core i9", 
                "AMD Ryzen 7", "AMD Ryzen 9",
                "Apple M1", "Apple M2", "Apple M3", "Apple M4"
            ])
        ),
        salience=100
    )
    def exclure_entree_gamme_cpu_puissant(self):
        """Exclut l'entrée de gamme si CPU puissant."""
        self.declare(GammeExclue(gamme="Entree de gamme", raison="CPU trop puissant"))
    
    @Rule(
        SpecificationPC(
            ram=P(lambda x: x in ["32 Go", "64 Go ou plus"])
        ),
        salience=100
    )
    def exclure_entree_gamme_ram_elevee(self):
        """Exclut l'entrée de gamme si RAM élevée."""
        self.declare(GammeExclue(gamme="Entree de gamme", raison="RAM trop elevee"))
    
    @Rule(
        SpecificationPC(
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
                "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                "Carte professionnelle (Quadro, RTX A series)"
            ])
        ),
        salience=100
    )
    def exclure_entree_gamme_gpu_puissant(self):
        """Exclut l'entrée de gamme si GPU puissant."""
        self.declare(GammeExclue(gamme="Entree de gamme", raison="GPU trop puissant"))
    
    @Rule(
        SpecificationPC(
            marque=P(lambda x: x in ["Apple", "Razer"])
        ),
        salience=100
    )
    def exclure_entree_gamme_marque_premium(self):
        """Exclut l'entrée de gamme si marque premium."""
        self.declare(GammeExclue(gamme="Entree de gamme", raison="Marque premium"))
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9", "Apple M2", "Apple M3", "Apple M4"])
        ),
        salience=100
    )
    def exclure_petit_budget_cpu_haut_gamme(self):
        """Exclut le petit budget si CPU très haut de gamme."""
        self.declare(GammeExclue(gamme="Petit budget", raison="CPU haut de gamme"))
    
    @Rule(
        SpecificationPC(
            ecran=P(lambda x: x in ["4K UHD (3840x2160)", "OLED 4K"])
        ),
        salience=100
    )
    def exclure_petit_budget_ecran_4k(self):
        """Exclut le petit budget si écran 4K."""
        self.declare(GammeExclue(gamme="Petit budget", raison="Ecran 4K"))
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Celeron / Pentium"])
        ),
        salience=100
    )
    def exclure_milieu_gamme_cpu_faible(self):
        """Exclut le milieu de gamme si CPU faible."""
        self.declare(GammeExclue(gamme="Milieu/haut de gamme", raison="CPU trop faible"))
        self.declare(GammeExclue(gamme="Haut de gamme / Createur", raison="CPU trop faible"))
        self.declare(GammeExclue(gamme="Premium / Workstation", raison="CPU trop faible"))
    
    @Rule(
        SpecificationPC(
            ram=P(lambda x: x in ["4 Go", "8 Go"])
        ),
        salience=100
    )
    def exclure_haut_gamme_ram_faible(self):
        """Exclut le haut de gamme si RAM faible."""
        self.declare(GammeExclue(gamme="Milieu/haut de gamme", raison="RAM insuffisante"))
        self.declare(GammeExclue(gamme="Haut de gamme / Createur", raison="RAM insuffisante"))
        self.declare(GammeExclue(gamme="Premium / Workstation", raison="RAM insuffisante"))
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in [
                "Intel Celeron / Pentium", "Intel Core i3", "Intel Core i5",
                "AMD Ryzen 3", "AMD Ryzen 5"
            ])
        ),
        salience=100
    )
    def exclure_premium_cpu_insuffisant(self):
        """Exclut le premium si CPU insuffisant."""
        self.declare(GammeExclue(gamme="Premium / Workstation", raison="CPU insuffisant pour premium"))
    
    @Rule(
        SpecificationPC(
            carte_graphique=P(lambda x: x == "Graphique integre (Intel UHD, AMD Radeon integre)")
        ),
        salience=100
    )
    def exclure_premium_gpu_integre(self):
        """Exclut le premium si GPU intégré basique."""
        self.declare(GammeExclue(gamme="Premium / Workstation", raison="GPU integre insuffisant"))
    
    # ============================================================
    # REGLES D'ESTIMATION - ENTREE DE GAMME (< 500€)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i3", "AMD Ryzen 3", "Intel Celeron / Pentium"]),
            ram=P(lambda x: x in ["4 Go", "8 Go"]),
            carte_graphique=P(lambda x: x == "Graphique integre (Intel UHD, AMD Radeon integre)")
        ),
        NOT(GammeExclue(gamme="Entree de gamme")),
        salience=50
    )
    def regle_entree_de_gamme(self):
        """Règle pour PC entrée de gamme (< 500€)."""
        self._ajouter_estimation(
            gamme="Entree de gamme",
            prix_min=0,
            prix_max=499,
            confiance=0.85,
            description="PC basique pour usage leger"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i3", "AMD Ryzen 3", "Intel Celeron / Pentium"]),
            ram=P(lambda x: x in ["4 Go", "8 Go"]),
            stockage=P(lambda x: x in ["HDD uniquement", "SSD 256 Go"]),
            usage=L("Bureautique")
        ),
        NOT(GammeExclue(gamme="Entree de gamme")),
        salience=55
    )
    def regle_entree_de_gamme_bureautique(self):
        """Règle pour PC bureautique entrée de gamme."""
        self._ajouter_estimation(
            gamme="Entree de gamme",
            prix_min=0,
            prix_max=499,
            confiance=0.90,
            description="PC bureautique basique"
        )
    
    # ============================================================
    # REGLES D'ESTIMATION - PETIT BUDGET (500-799€)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i3", "Intel Core i5", "AMD Ryzen 3", "AMD Ryzen 5"]),
            ram=L("8 Go"),
            carte_graphique=P(lambda x: x in [
                "Graphique integre (Intel UHD, AMD Radeon integre)",
                "NVIDIA GTX serie (GTX 1650, 1660)"
            ])
        ),
        NOT(GammeExclue(gamme="Petit budget")),
        salience=50
    )
    def regle_petit_budget(self):
        """Règle pour PC petit budget (500-799€)."""
        self._ajouter_estimation(
            gamme="Petit budget",
            prix_min=500,
            prix_max=799,
            confiance=0.80,
            description="PC polyvalent pour usage quotidien"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i5", "AMD Ryzen 5"]),
            ram=L("8 Go"),
            stockage=P(lambda x: x in ["SSD 256 Go", "SSD 512 Go"]),
            ecran=L("Full HD (1920x1080)")
        ),
        NOT(GammeExclue(gamme="Petit budget")),
        salience=55
    )
    def regle_petit_budget_multimedia(self):
        """Règle pour PC multimédia petit budget."""
        self._ajouter_estimation(
            gamme="Petit budget",
            prix_min=500,
            prix_max=799,
            confiance=0.85,
            description="PC multimedia polyvalent"
        )
    
    # ============================================================
    # REGLES D'ESTIMATION - BON RAPPORT QUALITE/PRIX (800-1199€)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1"]),
            ram=P(lambda x: x in ["8 Go", "16 Go"])
        ),
        NOT(GammeExclue(gamme="Bon rapport qualite/prix")),
        salience=50
    )
    def regle_bon_rapport_qualite_prix(self):
        """Règle pour PC bon rapport qualité/prix (800-1199€)."""
        self._ajouter_estimation(
            gamme="Bon rapport qualite/prix",
            prix_min=800,
            prix_max=1199,
            confiance=0.78,
            description="PC performant pour la plupart des usages"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7"]),
            ram=L("16 Go"),
            stockage=P(lambda x: x in ["SSD 512 Go", "SSD 1 To"]),
            carte_graphique=P(lambda x: x in [
                "NVIDIA GTX serie (GTX 1650, 1660)",
                "NVIDIA RTX entree de gamme (RTX 3050, 4050)"
            ])
        ),
        NOT(GammeExclue(gamme="Bon rapport qualite/prix")),
        salience=60
    )
    def regle_bon_rapport_qualite_prix_gaming_leger(self):
        """Règle pour PC gaming léger bon rapport qualité/prix."""
        self._ajouter_estimation(
            gamme="Bon rapport qualite/prix",
            prix_min=800,
            prix_max=1199,
            confiance=0.88,
            description="PC gaming leger ou creation"
        )
    
    @Rule(
        SpecificationPC(
            marque=L("Apple"),
            processeur=P(lambda x: x in ["Apple M1", "Apple M2"]),
            ram=P(lambda x: x in ["8 Go", "16 Go"])
        ),
        NOT(GammeExclue(gamme="Bon rapport qualite/prix")),
        salience=65
    )
    def regle_macbook_air_base(self):
        """Règle pour MacBook Air configuration de base."""
        self._ajouter_estimation(
            gamme="Bon rapport qualite/prix",
            prix_min=800,
            prix_max=1199,
            confiance=0.92,
            description="MacBook Air configuration de base"
        )
    
    # ============================================================
    # REGLES D'ESTIMATION - MILIEU/HAUT DE GAMME (1200-1799€)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1", "Apple M2"]),
            ram=P(lambda x: x in ["16 Go", "32 Go"])
        ),
        NOT(GammeExclue(gamme="Milieu/haut de gamme")),
        salience=50
    )
    def regle_milieu_haut_gamme(self):
        """Règle pour PC milieu/haut de gamme (1200-1799€)."""
        self._ajouter_estimation(
            gamme="Milieu/haut de gamme",
            prix_min=1200,
            prix_max=1799,
            confiance=0.75,
            description="PC performant pour gaming et creation"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i7", "AMD Ryzen 7"]),
            ram=L("16 Go"),
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX entree de gamme (RTX 3050, 4050)",
                "NVIDIA RTX milieu de gamme (RTX 3060, 4060)"
            ]),
            usage=L("Gaming")
        ),
        NOT(GammeExclue(gamme="Milieu/haut de gamme")),
        salience=70
    )
    def regle_gaming_milieu_gamme(self):
        """Règle pour PC Gaming milieu de gamme."""
        self._ajouter_estimation(
            gamme="Milieu/haut de gamme",
            prix_min=1200,
            prix_max=1799,
            confiance=0.90,
            description="PC Gaming performant"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i7", "AMD Ryzen 7"]),
            ram=P(lambda x: x in ["16 Go", "32 Go"]),
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
                "AMD Radeon RX dedie"
            ]),
            ecran=P(lambda x: x in ["Full HD (1920x1080)", "2.5K / QHD (2560x1440)", "OLED Full HD"]),
            taux_rafraichissement=P(lambda x: x in ["120 Hz", "144 Hz", "165 Hz ou plus"])
        ),
        NOT(GammeExclue(gamme="Milieu/haut de gamme")),
        salience=75
    )
    def regle_gaming_performant(self):
        """Règle pour PC Gaming performant avec écran rapide."""
        self._ajouter_estimation(
            gamme="Milieu/haut de gamme",
            prix_min=1200,
            prix_max=1799,
            confiance=0.93,
            description="PC Gaming avec ecran haute frequence"
        )
    
    # ============================================================
    # REGLES D'ESTIMATION - HAUT DE GAMME / CREATEUR (1800-2499€)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i7", "Intel Core i9", "AMD Ryzen 7", "AMD Ryzen 9", "Apple M2", "Apple M3"]),
            ram=P(lambda x: x in ["16 Go", "32 Go"])
        ),
        NOT(GammeExclue(gamme="Haut de gamme / Createur")),
        salience=50
    )
    def regle_haut_gamme_createur(self):
        """Règle pour PC haut de gamme créateur (1800-2499€)."""
        self._ajouter_estimation(
            gamme="Haut de gamme / Createur",
            prix_min=1800,
            prix_max=2499,
            confiance=0.75,
            description="PC haute performance pour professionnels"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9", "Apple M2", "Apple M3"]),
            ram=L("32 Go"),
            stockage=P(lambda x: x in ["SSD 1 To", "SSD 2 To ou plus"]),
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
                "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                "GPU integre Apple (M1/M2/M3/M4)"
            ])
        ),
        NOT(GammeExclue(gamme="Haut de gamme / Createur")),
        salience=70
    )
    def regle_creation_professionnelle(self):
        """Règle pour PC création professionnelle."""
        self._ajouter_estimation(
            gamme="Haut de gamme / Createur",
            prix_min=1800,
            prix_max=2499,
            confiance=0.88,
            description="PC creation video, 3D et photo professionnel"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9"]),
            ram=L("32 Go"),
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)"
            ]),
            usage=L("Gaming")
        ),
        NOT(GammeExclue(gamme="Haut de gamme / Createur")),
        salience=75
    )
    def regle_gaming_haut_gamme(self):
        """Règle pour PC Gaming haut de gamme."""
        self._ajouter_estimation(
            gamme="Haut de gamme / Createur",
            prix_min=1800,
            prix_max=2499,
            confiance=0.90,
            description="PC Gaming haut de gamme"
        )
    
    @Rule(
        SpecificationPC(
            marque=L("Apple"),
            processeur=P(lambda x: x in ["Apple M2", "Apple M3"]),
            ram=P(lambda x: x in ["16 Go", "32 Go"]),
            stockage=P(lambda x: x in ["SSD 512 Go", "SSD 1 To"])
        ),
        NOT(GammeExclue(gamme="Haut de gamme / Createur")),
        salience=70
    )
    def regle_macbook_pro(self):
        """Règle pour MacBook Pro."""
        self._ajouter_estimation(
            gamme="Haut de gamme / Createur",
            prix_min=1800,
            prix_max=2499,
            confiance=0.92,
            description="MacBook Pro pour professionnels"
        )
    
    # ============================================================
    # REGLES D'ESTIMATION - PREMIUM / WORKSTATION (> 2500€)
    # ============================================================
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9", "Apple M3", "Apple M4"]),
            ram=P(lambda x: x in ["32 Go", "64 Go ou plus"])
        ),
        NOT(GammeExclue(gamme="Premium / Workstation")),
        salience=50
    )
    def regle_premium_workstation(self):
        """Règle pour PC premium/workstation (> 2500€)."""
        self._ajouter_estimation(
            gamme="Premium / Workstation",
            prix_min=2500,
            prix_max=10000,
            confiance=0.78,
            description="PC ultra haut de gamme"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9", "Apple M3", "Apple M4"]),
            ram=P(lambda x: x in ["32 Go", "64 Go ou plus"]),
            stockage=P(lambda x: x in ["SSD 1 To", "SSD 2 To ou plus"]),
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                "Carte professionnelle (Quadro, RTX A series)",
                "GPU integre Apple (M1/M2/M3/M4)"
            ])
        ),
        NOT(GammeExclue(gamme="Premium / Workstation")),
        salience=70
    )
    def regle_workstation_professionnelle(self):
        """Règle pour Workstation professionnelle."""
        self._ajouter_estimation(
            gamme="Premium / Workstation",
            prix_min=2500,
            prix_max=10000,
            confiance=0.90,
            description="Workstation pour usage intensif"
        )
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9"]),
            ram=L("64 Go ou plus"),
            carte_graphique=P(lambda x: x in [
                "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                "Carte professionnelle (Quadro, RTX A series)"
            ]),
            ecran=P(lambda x: x in ["4K UHD (3840x2160)", "OLED 4K"])
        ),
        NOT(GammeExclue(gamme="Premium / Workstation")),
        salience=80
    )
    def regle_workstation_ultime(self):
        """Règle pour Workstation ultime."""
        self._ajouter_estimation(
            gamme="Premium / Workstation",
            prix_min=3000,
            prix_max=10000,
            confiance=0.95,
            description="Workstation ultime pour rendu 3D et IA"
        )
    
    @Rule(
        SpecificationPC(
            marque=L("Apple"),
            processeur=P(lambda x: x in ["Apple M3", "Apple M4"]),
            ram=P(lambda x: x in ["32 Go", "64 Go ou plus"]),
            stockage=P(lambda x: x in ["SSD 1 To", "SSD 2 To ou plus"])
        ),
        NOT(GammeExclue(gamme="Premium / Workstation")),
        salience=75
    )
    def regle_macbook_pro_max(self):
        """Règle pour MacBook Pro Max."""
        self._ajouter_estimation(
            gamme="Premium / Workstation",
            prix_min=2500,
            prix_max=10000,
            confiance=0.93,
            description="MacBook Pro Max pour professionnels exigeants"
        )
    
    # ============================================================
    # METHODES UTILITAIRES
    # ============================================================
    
    def _ajouter_estimation(self, gamme: str, prix_min: int, prix_max: int, 
                            confiance: float, description: str):
        """
        Ajoute une estimation à la liste des résultats.
        
        Vérifie si une estimation pour cette gamme existe déjà
        et garde celle avec la meilleure confiance.
        
        Args:
            gamme: Nom de la gamme de prix
            prix_min: Prix minimum
            prix_max: Prix maximum
            confiance: Score de confiance
            description: Description de la gamme
        """
        # Vérifier si cette gamme existe déjà
        for i, est in enumerate(self.estimations):
            if est["gamme"] == gamme:
                # Garder la meilleure confiance
                if confiance > est["confiance"]:
                    self.estimations[i] = {
                        "gamme": gamme,
                        "prix_min": prix_min,
                        "prix_max": prix_max,
                        "confiance": confiance,
                        "description": description
                    }
                return
        
        # Nouvelle estimation
        self.estimations.append({
            "gamme": gamme,
            "prix_min": prix_min,
            "prix_max": prix_max,
            "confiance": confiance,
            "description": description
        })
    
    def obtenir_estimations(self) -> list:
        """
        Retourne les estimations triées par confiance décroissante.
        
        Returns:
            Liste des estimations triées
        """
        return sorted(self.estimations, key=lambda x: x["confiance"], reverse=True)
    
    def reinitialiser_estimations(self):
        """Réinitialise la liste des estimations."""
        self.estimations = []
    
    def afficher_resultats(self, max_resultats: int = 3):
        """
        Affiche les résultats de manière formatée.
        
        Args:
            max_resultats: Nombre maximum de résultats à afficher
        """
        estimations = self.obtenir_estimations()
        
        print("\n" + "=" * 65)
        print("    RESULTATS DE L'ESTIMATION (Experta)")
        print("=" * 65)
        
        if not estimations:
            print("\n[?] Aucune estimation ne correspond aux specifications.")
            print("    Verifiez les specifications ou consultez les sites marchands.")
        else:
            nb_resultats = min(max_resultats, len(estimations))
            print(f"\n[>] {nb_resultats} estimation(s) possible(s) :\n")
            
            for i, est in enumerate(estimations[:nb_resultats], 1):
                pourcentage = est["confiance"] * 100
                
                if pourcentage >= 80:
                    indicateur = "[***] Forte probabilite"
                elif pourcentage >= 60:
                    indicateur = "[**]  Probabilite moyenne"
                else:
                    indicateur = "[*]   Faible probabilite"
                
                if est["prix_max"] >= 10000:
                    prix_str = f"> {est['prix_min']} euros"
                else:
                    prix_str = f"{est['prix_min']} - {est['prix_max']} euros"
                
                print(f"  {i}. {est['gamme']}")
                print(f"     Fourchette de prix : {prix_str}")
                print(f"     Confiance : {pourcentage:.1f}% - {indicateur}")
                print(f"     Description : {est['description']}")
                print()
        
        print("-" * 65)
        print("RAPPEL : Cette estimation est INDICATIVE uniquement.")
        print("=" * 65)


# ============================================================
# FONCTION UTILITAIRE POUR TESTS
# ============================================================

def tester_systeme():
    """Fonction de test du système expert."""
    print("\n=== TEST DU SYSTEME EXPERT EXPERTA ===\n")
    
    # Créer le moteur
    engine = SystemeExpertPrixPC()
    engine.reset()
    
    # Déclarer les spécifications
    engine.declare(SpecificationPC(
        taille_ecran="15.6 pouces",
        usage="Gaming",
        processeur="Intel Core i7",
        generation_cpu="Derniere generation (2024-2025)",
        ram="16 Go",
        stockage="SSD 1 To",
        carte_graphique="NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
        ecran="Full HD (1920x1080)",
        taux_rafraichissement="144 Hz",
        marque="ASUS",
        poids="Standard (plus de 2 kg)",
        pave_numerique=True,
        clavier_retroeclaire=True,
        clavier_rgb=True,
        thunderbolt=False,
        webcam_hd=True,
        lecteur_empreinte=False
    ))
    
    # Exécuter l'inférence
    engine.run()
    
    # Afficher les résultats
    engine.afficher_resultats()


if __name__ == "__main__":
    tester_systeme()
