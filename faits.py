#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Faits (Facts) - Système Expert Prix PC Portable
=================================================

Ce module définit les classes Fact utilisées par Experta pour
représenter les spécifications d'un PC portable.

Chaque classe Fact hérite de experta.Fact et représente
une catégorie d'information sur le PC à évaluer.

Classes:
    - SpecificationPC: Fait principal contenant toutes les specs
    - Estimation: Fait résultat contenant l'estimation de prix

Usage:
    >>> from experta import *
    >>> from faits import SpecificationPC
    >>> 
    >>> spec = SpecificationPC(
    ...     processeur="Intel Core i7",
    ...     ram="16 Go",
    ...     carte_graphique="NVIDIA RTX 4060"
    ... )
"""

from experta import Fact


# ============================================================
# CLASSES FACT POUR LES SPECIFICATIONS PC
# ============================================================

class SpecificationPC(Fact):
    """
    Fait représentant les spécifications d'un PC portable.
    
    Cette classe Fact stocke toutes les caractéristiques du PC
    renseignées par l'utilisateur.
    
    Attributes:
        taille_ecran (str): Taille de l'écran (ex: "15.6 pouces")
        usage (str): Usage principal prévu
        processeur (str): Type de processeur
        generation_cpu (str): Génération du CPU
        ram (str): Quantité de RAM
        stockage (str): Type et capacité de stockage
        carte_graphique (str): Type de carte graphique
        ecran (str): Définition de l'écran
        taux_rafraichissement (str): Taux de rafraîchissement
        marque (str): Marque du PC
        poids (str): Catégorie de poids
        pave_numerique (bool): Présence d'un pavé numérique
        clavier_retroeclaire (bool): Clavier rétroéclairé
        clavier_rgb (bool): Clavier RGB
        thunderbolt (bool): Port Thunderbolt
        webcam_hd (bool): Webcam HD
        lecteur_empreinte (bool): Lecteur d'empreintes
    """
    pass


class Estimation(Fact):
    """
    Fait représentant une estimation de prix.
    
    Ce fait est généré par le moteur d'inférence quand
    une règle d'estimation est déclenchée.
    
    Attributes:
        gamme (str): Nom de la gamme de prix
        prix_min (int): Prix minimum en euros
        prix_max (int): Prix maximum en euros
        confiance (float): Score de confiance (0-1)
        description (str): Description de la gamme
    """
    pass


class GammeExclue(Fact):
    """
    Fait indiquant qu'une gamme de prix est exclue.
    
    Ce fait est ajouté quand des conditions excluantes
    sont détectées pour une gamme spécifique.
    
    Attributes:
        gamme (str): Nom de la gamme exclue
        raison (str): Raison de l'exclusion
    """
    pass


# ============================================================
# OPTIONS DISPONIBLES POUR CHAQUE CARACTERISTIQUE
# ============================================================

OPTIONS = {
    "taille_ecran": [
        "14 pouces",
        "15.6 pouces",
        "16 pouces",
        "17 pouces ou plus"
    ],
    
    "usage": [
        "Bureautique",
        "Multimedia",
        "Gaming",
        "Creation (video, 3D, photo)",
        "Professionnel / Developpement"
    ],
    
    "processeur": [
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
    ],
    
    "generation_cpu": [
        "Ancienne generation (avant 2022)",
        "Generation recente (2022-2023)",
        "Derniere generation (2024-2025)",
        "Ne sait pas"
    ],
    
    "ram": [
        "4 Go",
        "8 Go",
        "16 Go",
        "32 Go",
        "64 Go ou plus"
    ],
    
    "stockage": [
        "HDD uniquement",
        "SSD 256 Go",
        "SSD 512 Go",
        "SSD 1 To",
        "SSD 2 To ou plus"
    ],
    
    "carte_graphique": [
        "Graphique integre (Intel UHD, AMD Radeon integre)",
        "GPU integre Apple (M1/M2/M3/M4)",
        "NVIDIA GTX serie (GTX 1650, 1660)",
        "NVIDIA RTX entree de gamme (RTX 3050, 4050)",
        "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
        "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
        "AMD Radeon RX dedie",
        "Carte professionnelle (Quadro, RTX A series)"
    ],
    
    "ecran": [
        "HD (1366x768)",
        "Full HD (1920x1080)",
        "2.5K / QHD (2560x1440)",
        "4K UHD (3840x2160)",
        "OLED Full HD",
        "OLED 4K"
    ],
    
    "taux_rafraichissement": [
        "60 Hz",
        "90 Hz",
        "120 Hz",
        "144 Hz",
        "165 Hz ou plus"
    ],
    
    "marque": [
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
    ],
    
    "poids": [
        "Ultraportable (moins de 1.3 kg)",
        "Leger (1.3 kg - 2 kg)",
        "Standard (plus de 2 kg)"
    ]
}

# Options booléennes
OPTIONS_BOOLEENNES = [
    "pave_numerique",
    "clavier_retroeclaire",
    "clavier_rgb",
    "thunderbolt",
    "webcam_hd",
    "lecteur_empreinte"
]


def obtenir_options(caracteristique: str) -> list:
    """
    Retourne la liste des options pour une caractéristique donnée.
    
    Args:
        caracteristique: Nom de la caractéristique
        
    Returns:
        Liste des options disponibles
    """
    return OPTIONS.get(caracteristique, [])


def est_option_booleenne(caracteristique: str) -> bool:
    """
    Vérifie si une caractéristique est de type booléen.
    
    Args:
        caracteristique: Nom de la caractéristique
        
    Returns:
        True si c'est une option booléenne
    """
    return caracteristique in OPTIONS_BOOLEENNES
