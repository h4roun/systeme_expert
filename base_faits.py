#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base de Faits - Systeme Expert Prix PC Portable
================================================

Ce module contient la classe BaseFaits qui gere :
- La definition des options possibles pour chaque caracteristique
- La collecte des specifications aupres de l'utilisateur (faits)
- Le stockage des faits collectes

La base de faits represente l'ensemble des informations connues
sur le PC a evaluer, collectees via le questionnaire utilisateur.
"""

from typing import List, Dict, Any


class BaseFaits:
    """
    Classe gerant la base de faits du systeme expert.
    
    La base de faits contient toutes les specifications du PC
    renseignees par l'utilisateur via le questionnaire interactif.
    
    Attributes:
        faits (Dict[str, Any]): Dictionnaire des specifications collectees
        options_* (List[str]): Listes des options possibles pour chaque caracteristique
    """
    
    def __init__(self):
        """Initialise la base de faits avec les options possibles."""
        
        # Dictionnaire pour stocker les faits (specifications de l'utilisateur)
        self.faits: Dict[str, Any] = {}
        
        # ============================================================
        # DEFINITION DES OPTIONS POUR CHAQUE CARACTERISTIQUE
        # ============================================================
        
        self.options_taille_ecran = [
            "14 pouces",
            "15.6 pouces",
            "16 pouces",
            "17 pouces ou plus"
        ]
        
        self.options_usage = [
            "Bureautique",
            "Multimedia",
            "Gaming",
            "Creation (video, 3D, photo)",
            "Professionnel / Developpement"
        ]
        
        self.options_processeur = [
            "Intel Core i3",
            "Intel Core i5",
            "Intel Core i7",
            "Intel Core i9",
            "AMD Ryzen 3",
            "AMD Ryzen 5",
            "AMD Ryzen 7",
            "AMD Ryzen 9",
            "Apple M1",
            "Apple M2",
            "Apple M3",
            "Apple M4",
            "Intel Celeron / Pentium",
            "Autre / Ne sait pas"
        ]
        
        self.options_generation_cpu = [
            "Ancienne generation (avant 2022)",
            "Generation recente (2022-2023)",
            "Derniere generation (2024-2025)",
            "Ne sait pas"
        ]
        
        self.options_ram = [
            "4 Go",
            "8 Go",
            "16 Go",
            "32 Go",
            "64 Go ou plus"
        ]
        
        self.options_stockage = [
            "HDD uniquement",
            "SSD 256 Go",
            "SSD 512 Go",
            "SSD 1 To",
            "SSD 2 To ou plus"
        ]
        
        self.options_carte_graphique = [
            "Graphique integre (Intel UHD, AMD Radeon integre)",
            "GPU integre Apple (M1/M2/M3/M4)",
            "NVIDIA GTX serie (GTX 1650, 1660)",
            "NVIDIA RTX entree de gamme (RTX 3050, 4050)",
            "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
            "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
            "AMD Radeon RX dedie",
            "Carte professionnelle (Quadro, RTX A series)"
        ]
        
        self.options_ecran = [
            "HD (1366x768)",
            "Full HD (1920x1080)",
            "2.5K / QHD (2560x1440)",
            "4K UHD (3840x2160)",
            "OLED Full HD",
            "OLED 4K"
        ]
        
        self.options_taux_rafraichissement = [
            "60 Hz",
            "90 Hz",
            "120 Hz",
            "144 Hz",
            "165 Hz ou plus"
        ]
        
        self.options_marque = [
            "Acer",
            "ASUS",
            "Apple",
            "Dell",
            "HP",
            "Lenovo",
            "MSI",
            "Razer",
            "Samsung",
            "Autre marque"
        ]
        
        self.options_poids = [
            "Ultraportable (moins de 1.3 kg)",
            "Leger (1.3 kg - 2 kg)",
            "Standard (plus de 2 kg)"
        ]
        
        # Liste des options booleennes (oui/non)
        self.options_booleennes = [
            "pave_numerique",
            "clavier_retroeclaire",
            "clavier_rgb",
            "thunderbolt",
            "webcam_hd",
            "lecteur_empreinte"
        ]
    
    def poser_question_oui_non(self, question: str) -> bool:
        """
        Pose une question oui/non a l'utilisateur.
        
        Args:
            question: La question a poser
            
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
                print("[!] Reponse non valide. Veuillez repondre par 'oui' ou 'non'.")
    
    def poser_question_choix(self, question: str, options: List[str]) -> str:
        """
        Pose une question a choix multiples a l'utilisateur.
        
        Args:
            question: La question a poser
            options: Liste des options possibles
            
        Returns:
            L'option choisie par l'utilisateur
        """
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                choix = input("Votre choix (numero) : ").strip()
                index = int(choix) - 1
                
                if 0 <= index < len(options):
                    return options[index]
                else:
                    print(f"[!] Veuillez entrer un numero entre 1 et {len(options)}.")
            except ValueError:
                print("[!] Veuillez entrer un numero valide.")
    
    def collecter_faits(self) -> None:
        """
        Collecte toutes les specifications du PC aupres de l'utilisateur.
        
        Cette methode implemente le chainage avant : elle collecte tous
        les faits d'abord, puis le moteur d'inference evaluera les regles.
        """
        print("\n" + "-" * 50)
        print("    QUESTIONNAIRE - SPECIFICATIONS DU PC")
        print("-" * 50)
        print("Repondez aux questions suivantes concernant le PC.\n")
        
        # Questions a choix multiples pour les specifications principales
        self.faits["taille_ecran"] = self.poser_question_choix(
            "Quelle est la taille de l'ecran ?",
            self.options_taille_ecran
        )
        
        self.faits["usage"] = self.poser_question_choix(
            "Quel est l'usage principal prevu ?",
            self.options_usage
        )
        
        self.faits["processeur"] = self.poser_question_choix(
            "Quel est le type de processeur ?",
            self.options_processeur
        )
        
        self.faits["generation_cpu"] = self.poser_question_choix(
            "Quelle est la generation du processeur ?",
            self.options_generation_cpu
        )
        
        self.faits["ram"] = self.poser_question_choix(
            "Quelle est la quantite de RAM ?",
            self.options_ram
        )
        
        self.faits["stockage"] = self.poser_question_choix(
            "Quel est le type et la capacite de stockage ?",
            self.options_stockage
        )
        
        self.faits["carte_graphique"] = self.poser_question_choix(
            "Quel est le type de carte graphique ?",
            self.options_carte_graphique
        )
        
        self.faits["ecran"] = self.poser_question_choix(
            "Quelle est la definition de l'ecran ?",
            self.options_ecran
        )
        
        self.faits["taux_rafraichissement"] = self.poser_question_choix(
            "Quel est le taux de rafraichissement de l'ecran ?",
            self.options_taux_rafraichissement
        )
        
        self.faits["marque"] = self.poser_question_choix(
            "Quelle est la marque du PC ?",
            self.options_marque
        )
        
        self.faits["poids"] = self.poser_question_choix(
            "Quelle est la categorie de poids du PC ?",
            self.options_poids
        )
        
        # Questions oui/non pour les options supplementaires
        print("\n--- Options supplementaires ---")
        
        self.faits["pave_numerique"] = self.poser_question_oui_non(
            "Le PC possede-t-il un pave numerique ?"
        )
        
        self.faits["clavier_retroeclaire"] = self.poser_question_oui_non(
            "Le clavier est-il retroeclaire ?"
        )
        
        self.faits["clavier_rgb"] = self.poser_question_oui_non(
            "Le clavier possede-t-il un eclairage RGB ?"
        )
        
        self.faits["thunderbolt"] = self.poser_question_oui_non(
            "Le PC possede-t-il un port Thunderbolt ?"
        )
        
        self.faits["webcam_hd"] = self.poser_question_oui_non(
            "Le PC possede-t-il une webcam HD ou superieure ?"
        )
        
        self.faits["lecteur_empreinte"] = self.poser_question_oui_non(
            "Le PC possede-t-il un lecteur d'empreintes digitales ?"
        )
        
        print("\n[OK] Specifications collectees. Analyse en cours...\n")
    
    def obtenir_fait(self, cle: str, defaut: Any = None) -> Any:
        """
        Recupere un fait de la base de faits.
        
        Args:
            cle: La cle du fait a recuperer
            defaut: Valeur par defaut si le fait n'existe pas
            
        Returns:
            La valeur du fait ou la valeur par defaut
        """
        return self.faits.get(cle, defaut)
    
    def ajouter_fait(self, cle: str, valeur: Any) -> None:
        """
        Ajoute ou modifie un fait dans la base de faits.
        
        Args:
            cle: La cle du fait
            valeur: La valeur du fait
        """
        self.faits[cle] = valeur
    
    def afficher_resume(self) -> None:
        """Affiche un resume des faits (specifications) collectes."""
        print("\n" + "-" * 50)
        print("    RESUME DES SPECIFICATIONS (BASE DE FAITS)")
        print("-" * 50)
        
        # Specifications principales
        specs_principales = [
            ("Taille ecran", "taille_ecran"),
            ("Usage", "usage"),
            ("Processeur", "processeur"),
            ("Generation CPU", "generation_cpu"),
            ("RAM", "ram"),
            ("Stockage", "stockage"),
            ("Carte graphique", "carte_graphique"),
            ("Definition ecran", "ecran"),
            ("Taux rafraichissement", "taux_rafraichissement"),
            ("Marque", "marque"),
            ("Poids", "poids")
        ]
        
        print("\nCaracteristiques principales :")
        for label, cle in specs_principales:
            valeur = self.faits.get(cle, "Non specifie")
            print(f"  - {label} : {valeur}")
        
        # Options booleennes
        options = [
            ("Pave numerique", "pave_numerique"),
            ("Clavier retroeclaire", "clavier_retroeclaire"),
            ("Clavier RGB", "clavier_rgb"),
            ("Thunderbolt", "thunderbolt"),
            ("Webcam HD", "webcam_hd"),
            ("Lecteur empreinte", "lecteur_empreinte")
        ]
        
        print("\nOptions :")
        for label, cle in options:
            valeur = "Oui" if self.faits.get(cle, False) else "Non"
            print(f"  - {label} : {valeur}")
        
        print("-" * 50)
    
    def reinitialiser(self) -> None:
        """Reinitialise la base de faits (vide tous les faits collectes)."""
        self.faits.clear()
