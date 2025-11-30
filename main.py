#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système Expert - Estimation du Prix d'un Ordinateur Portable
=============================================================

Point d'entrée principal du système expert utilisant la bibliothèque Experta.

Auteur: TP Universitaire - Intelligence Artificielle
Date: Novembre 2025

Description:
    Ce programme implémente un système expert utilisant Experta
    (inspiré de CLIPS) pour estimer la gamme de prix d'un ordinateur
    portable à partir de ses spécifications techniques.

Structure du projet:
    - main.py     : Point d'entrée et orchestration
    - faits.py    : Classes Fact pour les spécifications
    - regles.py   : KnowledgeEngine avec les règles d'estimation
    - gui.py      : Interface graphique Tkinter

Installation:
    pip install experta

Gammes de prix estimées:
    1. Entrée de gamme (< 500 euros)
    2. Petit budget (500 - 799 euros)
    3. Bon rapport qualité/prix (800 - 1199 euros)
    4. Milieu/haut de gamme (1200 - 1799 euros)
    5. Haut de gamme / Créateur (1800 - 2499 euros)
    6. Premium / Workstation (> 2500 euros)

AVERTISSEMENT:
    Ce système est UNIQUEMENT à but éducatif et pédagogique.
    Les estimations de prix sont INDICATIVES.
"""

from typing import List, Dict, Any
from faits import SpecificationPC, OPTIONS, OPTIONS_BOOLEENNES, obtenir_options
from regles import SystemeExpertPrixPC


class InterfaceConsole:
    """
    Interface console pour le système expert.
    
    Cette classe gère l'interaction avec l'utilisateur :
    - Questionnaire interactif
    - Collecte des spécifications
    - Lancement de l'inférence
    - Affichage des résultats
    """
    
    def __init__(self):
        """Initialise l'interface console."""
        self.specifications = {}
        self.engine = None
    
    def afficher_banniere(self):
        """Affiche la bannière du programme."""
        banniere = """
╔══════════════════════════════════════════════════════════════════════════════════════╗
║  ░██████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗███████╗                        ║
║  ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝                        ║
║  ╚█████╗  ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║█████╗                          ║
║   ╚═══██╗  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══╝                          ║
║  ██████╔╝   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║███████╗                        ║
║  ╚═════╝    ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝                        ║
║                                                                                      ║
║  ███████╗██╗  ██╗██████╗ ███████╗██████╗ ████████╗ █████╗                             ║
║  ██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗                            ║
║  █████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝   ██║   ███████║                            ║
║  ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ██╔══██║                            ║
║  ███████╗██╔╝ ██╗██║     ███████╗██║  ██║   ██║   ██║  ██║                            ║
║  ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                            ║
║                                                                                      ║
║  ┌─────────────────────────────────────────────────────────────────────────────────┐ ║
║  │  [SYSTEM]  ESTIMATION PRIX PC PORTABLE  ::  EXPERTA ENGINE v2.0                │ ║
║  │  [STATUS]  ONLINE  ::  RETE ALGORITHM  ::  KNOWLEDGE ENGINE LOADED             │ ║
║  └─────────────────────────────────────────────────────────────────────────────────┘ ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
"""
        print(banniere)
    
    def afficher_avertissement(self):
        """Affiche l'avertissement obligatoire."""
        print("\n" + "=" * 65)
        print("    ⚠️  AVERTISSEMENT IMPORTANT")
        print("=" * 65)
        print("Ce système expert est UNIQUEMENT à but ÉDUCATIF.")
        print("Les estimations de prix sont INDICATIVES et peuvent varier selon :")
        print("  • Les promotions et offres en cours")
        print("  • La disponibilité des produits")
        print("  • Le marché et la région d'achat")
        print("  • Les configurations exactes des modèles")
        print("Consultez les sites marchands pour des prix réels.")
        print("=" * 65 + "\n")
    
    def poser_question_choix(self, question: str, options: List[str]) -> str:
        """
        Pose une question à choix multiples.
        
        Args:
            question: La question à poser
            options: Liste des options possibles
            
        Returns:
            L'option choisie par l'utilisateur
        """
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                choix = input("Votre choix (numéro) : ").strip()
                index = int(choix) - 1
                
                if 0 <= index < len(options):
                    return options[index]
                else:
                    print(f"[!] Veuillez entrer un numéro entre 1 et {len(options)}.")
            except ValueError:
                print("[!] Veuillez entrer un numéro valide.")
    
    def poser_question_oui_non(self, question: str) -> bool:
        """
        Pose une question oui/non.
        
        Args:
            question: La question à poser
            
        Returns:
            True si oui, False si non
        """
        while True:
            reponse = input(f"{question} (oui/non) : ").strip().lower()
            
            if reponse in ["oui", "o", "yes", "y", "1"]:
                return True
            elif reponse in ["non", "n", "no", "0"]:
                return False
            else:
                print("[!] Réponse non valide. Veuillez répondre par 'oui' ou 'non'.")
    
    def collecter_specifications(self):
        """Collecte les spécifications via le questionnaire."""
        print("\n" + "-" * 50)
        print("    QUESTIONNAIRE - SPÉCIFICATIONS DU PC")
        print("-" * 50)
        print("Répondez aux questions suivantes concernant le PC.\n")
        
        # Questions principales
        questions = [
            ("taille_ecran", "Quelle est la taille de l'écran ?"),
            ("usage", "Quel est l'usage principal prévu ?"),
            ("processeur", "Quel est le type de processeur ?"),
            ("generation_cpu", "Quelle est la génération du processeur ?"),
            ("ram", "Quelle est la quantité de RAM ?"),
            ("stockage", "Quel est le type et la capacité de stockage ?"),
            ("carte_graphique", "Quel est le type de carte graphique ?"),
            ("ecran", "Quelle est la définition de l'écran ?"),
            ("taux_rafraichissement", "Quel est le taux de rafraîchissement ?"),
            ("marque", "Quelle est la marque du PC ?"),
            ("poids", "Quelle est la catégorie de poids du PC ?"),
        ]
        
        for cle, question in questions:
            options = obtenir_options(cle)
            self.specifications[cle] = self.poser_question_choix(question, options)
        
        # Questions booléennes
        print("\n--- Options supplémentaires ---")
        
        questions_bool = [
            ("pave_numerique", "Le PC possède-t-il un pavé numérique ?"),
            ("clavier_retroeclaire", "Le clavier est-il rétroéclairé ?"),
            ("clavier_rgb", "Le clavier possède-t-il un éclairage RGB ?"),
            ("thunderbolt", "Le PC possède-t-il un port Thunderbolt ?"),
            ("webcam_hd", "Le PC possède-t-il une webcam HD ou supérieure ?"),
            ("lecteur_empreinte", "Le PC possède-t-il un lecteur d'empreintes ?"),
        ]
        
        for cle, question in questions_bool:
            self.specifications[cle] = self.poser_question_oui_non(question)
        
        print("\n[OK] Spécifications collectées. Analyse en cours...\n")
    
    def afficher_resume_specifications(self):
        """Affiche un résumé des spécifications collectées."""
        print("\n" + "-" * 50)
        print("    RÉSUMÉ DES SPÉCIFICATIONS")
        print("-" * 50)
        
        # Spécifications principales
        specs_principales = [
            ("Taille écran", "taille_ecran"),
            ("Usage", "usage"),
            ("Processeur", "processeur"),
            ("Génération CPU", "generation_cpu"),
            ("RAM", "ram"),
            ("Stockage", "stockage"),
            ("Carte graphique", "carte_graphique"),
            ("Définition écran", "ecran"),
            ("Taux rafraîchissement", "taux_rafraichissement"),
            ("Marque", "marque"),
            ("Poids", "poids")
        ]
        
        print("\nCaractéristiques principales :")
        for label, cle in specs_principales:
            valeur = self.specifications.get(cle, "Non spécifié")
            print(f"  • {label} : {valeur}")
        
        # Options booléennes
        options = [
            ("Pavé numérique", "pave_numerique"),
            ("Clavier rétroéclairé", "clavier_retroeclaire"),
            ("Clavier RGB", "clavier_rgb"),
            ("Thunderbolt", "thunderbolt"),
            ("Webcam HD", "webcam_hd"),
            ("Lecteur empreinte", "lecteur_empreinte")
        ]
        
        print("\nOptions :")
        for label, cle in options:
            valeur = "Oui" if self.specifications.get(cle, False) else "Non"
            print(f"  • {label} : {valeur}")
        
        print("-" * 50)
    
    def lancer_inference(self):
        """Lance le moteur d'inférence Experta."""
        # Créer le moteur
        self.engine = SystemeExpertPrixPC()
        self.engine.reset()
        
        # Déclarer les spécifications comme un Fact
        self.engine.declare(SpecificationPC(**self.specifications))
        
        # Exécuter l'inférence (algorithme RETE)
        self.engine.run()
    
    def afficher_resultats(self):
        """Affiche les résultats de l'inférence."""
        self.engine.afficher_resultats()
        print("\nMerci d'avoir utilisé le système expert Experta !\n")
    
    def executer(self):
        """Exécute le cycle complet du système expert."""
        # Bannière
        self.afficher_banniere()
        
        # Avertissement
        self.afficher_avertissement()
        
        # Confirmation
        input("Appuyez sur Entrée pour commencer le questionnaire...")
        
        # Collecte
        self.collecter_specifications()
        
        # Résumé
        self.afficher_resume_specifications()
        
        # Inférence
        self.lancer_inference()
        
        # Résultats
        self.afficher_resultats()
    
    def reinitialiser(self):
        """Réinitialise l'interface pour une nouvelle estimation."""
        self.specifications = {}
        if self.engine:
            self.engine.reinitialiser_estimations()
            self.engine = None


def afficher_menu() -> str:
    """
    Affiche le menu principal.
    
    Returns:
        Le choix de l'utilisateur
    """
    print("\n" + "-" * 40)
    print("    MENU PRINCIPAL")
    print("-" * 40)
    print("  1. Lancer une estimation de prix")
    print("  2. Tester avec des valeurs prédéfinies")
    print("  3. Quitter")
    print("-" * 40)
    
    return input("Votre choix (1-3) : ").strip()


def test_predefined():
    """Lance un test avec des valeurs prédéfinies."""
    print("\n=== TEST AVEC VALEURS PRÉDÉFINIES ===\n")
    
    # Créer le moteur
    engine = SystemeExpertPrixPC()
    engine.reset()
    
    # Spécifications de test (PC Gaming)
    specs_test = {
        "taille_ecran": "15.6 pouces",
        "usage": "Gaming",
        "processeur": "Intel Core i7",
        "generation_cpu": "Derniere generation (2024-2025)",
        "ram": "16 Go",
        "stockage": "SSD 1 To",
        "carte_graphique": "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
        "ecran": "Full HD (1920x1080)",
        "taux_rafraichissement": "144 Hz",
        "marque": "ASUS",
        "poids": "Standard (plus de 2 kg)",
        "pave_numerique": True,
        "clavier_retroeclaire": True,
        "clavier_rgb": True,
        "thunderbolt": False,
        "webcam_hd": True,
        "lecteur_empreinte": False
    }
    
    print("Spécifications de test :")
    for cle, valeur in specs_test.items():
        print(f"  • {cle}: {valeur}")
    
    # Déclarer et exécuter
    engine.declare(SpecificationPC(**specs_test))
    engine.run()
    
    # Afficher les résultats
    engine.afficher_resultats()


def main():
    """Fonction principale du programme."""
    interface = InterfaceConsole()
    
    print("\n" + "=" * 65)
    print("    BIENVENUE DANS LE SYSTÈME EXPERT EXPERTA")
    print("    Estimation de Prix PC Portable")
    print("=" * 65)
    
    while True:
        choix = afficher_menu()
        
        if choix == "1":
            interface.reinitialiser()
            interface.executer()
        
        elif choix == "2":
            test_predefined()
        
        elif choix == "3":
            print("\nAu revoir !\n")
            break
        
        else:
            print("[!] Choix invalide. Veuillez entrer 1, 2 ou 3.")


# ============================================================
# POINT D'ENTRÉE DU PROGRAMME
# ============================================================

if __name__ == "__main__":
    main()
