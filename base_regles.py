#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base de Regles - Systeme Expert Prix PC Portable
=================================================

Ce module contient la classe BaseRegles qui gere :
- La definition des regles d'estimation de prix
- L'ajout de nouvelles regles
- L'acces aux regles pour le moteur d'inference

Chaque regle est composee de :
- nom : nom de la gamme de prix
- prix_min, prix_max : fourchette de prix en euros
- description : description de la gamme
- conditions_requises : conditions qui DOIVENT etre satisfaites
- conditions_optionnelles : conditions qui ajoutent un bonus de confiance
- conditions_excluantes : conditions qui EXCLUENT cette gamme
- confiance_base : niveau de confiance de base (0 a 1)
"""

from typing import List, Dict, Optional


class BaseRegles:
    """
    Classe gerant la base de regles du systeme expert.
    
    La base de regles contient toutes les regles permettant d'estimer
    la gamme de prix d'un PC portable selon ses specifications.
    
    Attributes:
        regles (List[Dict]): Liste des regles du systeme expert
    """
    
    def __init__(self):
        """Initialise la base de regles avec les regles predefinies."""
        self.regles: List[Dict] = self._creer_regles_initiales()
    
    def _creer_regles_initiales(self) -> List[Dict]:
        """
        Cree et retourne la liste des regles initiales du systeme.
        
        Returns:
            Liste des regles predefinies
        """
        return [
            # ============================================================
            # Regle 1: Entree de gamme (< 500 euros)
            # ============================================================
            {
                "nom": "Entree de gamme",
                "prix_min": 0,
                "prix_max": 499,
                "description": "PC basique pour usage leger",
                "conditions_requises": {
                    "processeur": ["Intel Core i3", "AMD Ryzen 3", "Intel Celeron / Pentium"],
                    "ram": ["4 Go", "8 Go"],
                    "carte_graphique": ["Graphique integre (Intel UHD, AMD Radeon integre)"]
                },
                "conditions_optionnelles": {
                    "stockage": ["HDD uniquement", "SSD 256 Go"],
                    "ecran": ["HD (1366x768)", "Full HD (1920x1080)"],
                    "usage": ["Bureautique"],
                    "generation_cpu": ["Ancienne generation (avant 2022)"]
                },
                "conditions_excluantes": {
                    "processeur": ["Intel Core i7", "Intel Core i9", "AMD Ryzen 7", "AMD Ryzen 9", 
                                   "Apple M1", "Apple M2", "Apple M3", "Apple M4"],
                    "ram": ["32 Go", "64 Go ou plus"],
                    "carte_graphique": ["NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
                                        "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                                        "Carte professionnelle (Quadro, RTX A series)"],
                    "marque": ["Apple", "Razer"]
                },
                "confiance_base": 0.75
            },
            
            # ============================================================
            # Regle 2: Petit budget (500 - 799 euros)
            # ============================================================
            {
                "nom": "Petit budget",
                "prix_min": 500,
                "prix_max": 799,
                "description": "PC polyvalent pour usage quotidien",
                "conditions_requises": {
                    "processeur": ["Intel Core i3", "Intel Core i5", "AMD Ryzen 3", "AMD Ryzen 5"],
                    "ram": ["8 Go"],
                    "carte_graphique": ["Graphique integre (Intel UHD, AMD Radeon integre)",
                                        "NVIDIA GTX serie (GTX 1650, 1660)"]
                },
                "conditions_optionnelles": {
                    "stockage": ["SSD 256 Go", "SSD 512 Go"],
                    "ecran": ["Full HD (1920x1080)"],
                    "usage": ["Bureautique", "Multimedia"],
                    "taux_rafraichissement": ["60 Hz"]
                },
                "conditions_excluantes": {
                    "processeur": ["Intel Core i9", "AMD Ryzen 9", "Apple M2", "Apple M3", "Apple M4"],
                    "ram": ["32 Go", "64 Go ou plus"],
                    "carte_graphique": ["NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                                        "Carte professionnelle (Quadro, RTX A series)"],
                    "ecran": ["4K UHD (3840x2160)", "OLED 4K"],
                    "marque": ["Apple", "Razer"]
                },
                "confiance_base": 0.78
            },
            
            # ============================================================
            # Regle 3: Bon rapport qualite/prix (800 - 1199 euros)
            # ============================================================
            {
                "nom": "Bon rapport qualite/prix",
                "prix_min": 800,
                "prix_max": 1199,
                "description": "PC performant pour la plupart des usages",
                "conditions_requises": {
                    "processeur": ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M1"],
                    "ram": ["8 Go", "16 Go"]
                },
                "conditions_optionnelles": {
                    "stockage": ["SSD 512 Go", "SSD 1 To"],
                    "carte_graphique": ["NVIDIA GTX serie (GTX 1650, 1660)",
                                        "NVIDIA RTX entree de gamme (RTX 3050, 4050)",
                                        "GPU integre Apple (M1/M2/M3/M4)"],
                    "ecran": ["Full HD (1920x1080)", "2.5K / QHD (2560x1440)"],
                    "usage": ["Multimedia", "Gaming", "Professionnel / Developpement"],
                    "taux_rafraichissement": ["120 Hz", "144 Hz"],
                    "generation_cpu": ["Generation recente (2022-2023)", "Derniere generation (2024-2025)"]
                },
                "conditions_excluantes": {
                    "processeur": ["Intel Celeron / Pentium"],
                    "ram": ["4 Go"],
                    "carte_graphique": ["NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                                        "Carte professionnelle (Quadro, RTX A series)"],
                    "ecran": ["OLED 4K"]
                },
                "confiance_base": 0.80
            },
            
            # ============================================================
            # Regle 4: Milieu/haut de gamme (1200 - 1799 euros)
            # ============================================================
            {
                "nom": "Milieu/haut de gamme",
                "prix_min": 1200,
                "prix_max": 1799,
                "description": "PC performant pour gaming et creation",
                "conditions_requises": {
                    "processeur": ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7", 
                                   "Apple M1", "Apple M2"],
                    "ram": ["16 Go", "32 Go"]
                },
                "conditions_optionnelles": {
                    "stockage": ["SSD 512 Go", "SSD 1 To"],
                    "carte_graphique": ["NVIDIA RTX entree de gamme (RTX 3050, 4050)",
                                        "NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
                                        "GPU integre Apple (M1/M2/M3/M4)",
                                        "AMD Radeon RX dedie"],
                    "ecran": ["Full HD (1920x1080)", "2.5K / QHD (2560x1440)", "OLED Full HD"],
                    "usage": ["Gaming", "Creation (video, 3D, photo)", "Professionnel / Developpement"],
                    "taux_rafraichissement": ["120 Hz", "144 Hz", "165 Hz ou plus"],
                    "generation_cpu": ["Generation recente (2022-2023)", "Derniere generation (2024-2025)"],
                    "pave_numerique": True,
                    "clavier_retroeclaire": True
                },
                "conditions_excluantes": {
                    "processeur": ["Intel Celeron / Pentium", "Intel Core i3", "AMD Ryzen 3"],
                    "ram": ["4 Go", "8 Go"],
                    "ecran": ["HD (1366x768)"]
                },
                "confiance_base": 0.82
            },
            
            # ============================================================
            # Regle 5: Haut de gamme / Createur (1800 - 2499 euros)
            # ============================================================
            {
                "nom": "Haut de gamme / Createur",
                "prix_min": 1800,
                "prix_max": 2499,
                "description": "PC haute performance pour professionnels et createurs",
                "conditions_requises": {
                    "processeur": ["Intel Core i7", "Intel Core i9", "AMD Ryzen 7", "AMD Ryzen 9",
                                   "Apple M2", "Apple M3"],
                    "ram": ["16 Go", "32 Go"]
                },
                "conditions_optionnelles": {
                    "stockage": ["SSD 1 To", "SSD 2 To ou plus"],
                    "carte_graphique": ["NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
                                        "NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                                        "GPU integre Apple (M1/M2/M3/M4)"],
                    "ecran": ["2.5K / QHD (2560x1440)", "4K UHD (3840x2160)", "OLED Full HD", "OLED 4K"],
                    "usage": ["Gaming", "Creation (video, 3D, photo)", "Professionnel / Developpement"],
                    "taux_rafraichissement": ["144 Hz", "165 Hz ou plus"],
                    "generation_cpu": ["Derniere generation (2024-2025)"],
                    "marque": ["Apple", "ASUS", "MSI", "Razer", "Dell"],
                    "thunderbolt": True,
                    "poids": ["Ultraportable (moins de 1.3 kg)", "Leger (1.3 kg - 2 kg)"]
                },
                "conditions_excluantes": {
                    "processeur": ["Intel Celeron / Pentium", "Intel Core i3", "AMD Ryzen 3"],
                    "ram": ["4 Go", "8 Go"],
                    "stockage": ["HDD uniquement", "SSD 256 Go"],
                    "ecran": ["HD (1366x768)"]
                },
                "confiance_base": 0.83
            },
            
            # ============================================================
            # Regle 6: Premium / Workstation (> 2500 euros)
            # ============================================================
            {
                "nom": "Premium / Workstation",
                "prix_min": 2500,
                "prix_max": 10000,
                "description": "PC ultra haut de gamme pour usage intensif",
                "conditions_requises": {
                    "processeur": ["Intel Core i9", "AMD Ryzen 9", "Apple M3", "Apple M4"],
                    "ram": ["32 Go", "64 Go ou plus"]
                },
                "conditions_optionnelles": {
                    "stockage": ["SSD 1 To", "SSD 2 To ou plus"],
                    "carte_graphique": ["NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)",
                                        "Carte professionnelle (Quadro, RTX A series)",
                                        "GPU integre Apple (M1/M2/M3/M4)"],
                    "ecran": ["4K UHD (3840x2160)", "OLED 4K"],
                    "usage": ["Creation (video, 3D, photo)", "Professionnel / Developpement"],
                    "taux_rafraichissement": ["144 Hz", "165 Hz ou plus"],
                    "generation_cpu": ["Derniere generation (2024-2025)"],
                    "marque": ["Apple", "Razer", "MSI"],
                    "thunderbolt": True
                },
                "conditions_excluantes": {
                    "processeur": ["Intel Celeron / Pentium", "Intel Core i3", "Intel Core i5",
                                   "AMD Ryzen 3", "AMD Ryzen 5"],
                    "ram": ["4 Go", "8 Go", "16 Go"],
                    "stockage": ["HDD uniquement", "SSD 256 Go"],
                    "carte_graphique": ["Graphique integre (Intel UHD, AMD Radeon integre)"],
                    "ecran": ["HD (1366x768)", "Full HD (1920x1080)"]
                },
                "confiance_base": 0.85
            },
            
            # ============================================================
            # Regle 7: Gaming milieu de gamme (regle specifique)
            # ============================================================
            {
                "nom": "Milieu/haut de gamme",
                "prix_min": 1200,
                "prix_max": 1799,
                "description": "PC Gaming performant",
                "conditions_requises": {
                    "usage": ["Gaming"],
                    "carte_graphique": ["NVIDIA RTX entree de gamme (RTX 3050, 4050)",
                                        "NVIDIA RTX milieu de gamme (RTX 3060, 4060)"],
                    "ram": ["16 Go"]
                },
                "conditions_optionnelles": {
                    "taux_rafraichissement": ["120 Hz", "144 Hz", "165 Hz ou plus"],
                    "processeur": ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7"],
                    "stockage": ["SSD 512 Go", "SSD 1 To"],
                    "clavier_rgb": True
                },
                "conditions_excluantes": {
                    "carte_graphique": ["Graphique integre (Intel UHD, AMD Radeon integre)"],
                    "taux_rafraichissement": ["60 Hz"]
                },
                "confiance_base": 0.84
            },
            
            # ============================================================
            # Regle 8: MacBook Air / Pro entree de gamme
            # ============================================================
            {
                "nom": "Bon rapport qualite/prix",
                "prix_min": 800,
                "prix_max": 1199,
                "description": "MacBook Air configuration de base",
                "conditions_requises": {
                    "marque": ["Apple"],
                    "processeur": ["Apple M1", "Apple M2"],
                    "ram": ["8 Go", "16 Go"]
                },
                "conditions_optionnelles": {
                    "stockage": ["SSD 256 Go", "SSD 512 Go"],
                    "poids": ["Ultraportable (moins de 1.3 kg)", "Leger (1.3 kg - 2 kg)"]
                },
                "conditions_excluantes": {
                    "ram": ["32 Go", "64 Go ou plus"],
                    "processeur": ["Apple M3", "Apple M4"]
                },
                "confiance_base": 0.88
            }
        ]
    
    def obtenir_regles(self) -> List[Dict]:
        """
        Retourne la liste de toutes les regles.
        
        Returns:
            Liste des regles du systeme expert
        """
        return self.regles
    
    def obtenir_regle_par_nom(self, nom: str) -> Optional[Dict]:
        """
        Recherche une regle par son nom.
        
        Args:
            nom: Le nom de la gamme de prix recherchee
            
        Returns:
            La premiere regle correspondante ou None
        """
        for regle in self.regles:
            if regle["nom"] == nom:
                return regle
        return None
    
    def ajouter_regle(self, nom: str, prix_min: int, prix_max: int,
                      description: str, conditions_requises: Dict,
                      conditions_optionnelles: Dict = None,
                      conditions_excluantes: Dict = None,
                      confiance_base: float = 0.75) -> None:
        """
        Ajoute une nouvelle regle a la base de regles.
        
        Args:
            nom: Nom de la gamme de prix
            prix_min: Prix minimum de la fourchette
            prix_max: Prix maximum de la fourchette
            description: Description de la gamme
            conditions_requises: Dict des conditions obligatoires
            conditions_optionnelles: Dict des conditions bonus (optionnel)
            conditions_excluantes: Dict des conditions excluantes (optionnel)
            confiance_base: Niveau de confiance de base (0 a 1)
        
        Example:
            >>> base_regles.ajouter_regle(
            ...     nom="Gaming Ultra",
            ...     prix_min=2000,
            ...     prix_max=3000,
            ...     description="PC Gaming tres haut de gamme",
            ...     conditions_requises={
            ...         "carte_graphique": ["NVIDIA RTX haut de gamme (RTX 4070, 4080, 4090)"],
            ...         "ram": ["32 Go", "64 Go ou plus"]
            ...     },
            ...     conditions_optionnelles={
            ...         "clavier_rgb": True
            ...     },
            ...     confiance_base=0.85
            ... )
        """
        nouvelle_regle = {
            "nom": nom,
            "prix_min": prix_min,
            "prix_max": prix_max,
            "description": description,
            "conditions_requises": conditions_requises,
            "conditions_optionnelles": conditions_optionnelles or {},
            "conditions_excluantes": conditions_excluantes or {},
            "confiance_base": confiance_base
        }
        
        self.regles.append(nouvelle_regle)
        print(f"[OK] Regle '{nom}' ajoutee avec succes!")
    
    def supprimer_regle(self, nom: str) -> bool:
        """
        Supprime une regle par son nom.
        
        Args:
            nom: Le nom de la regle a supprimer
            
        Returns:
            True si la regle a ete supprimee, False sinon
        """
        for i, regle in enumerate(self.regles):
            if regle["nom"] == nom:
                del self.regles[i]
                print(f"[OK] Regle '{nom}' supprimee avec succes!")
                return True
        
        print(f"[!] Regle '{nom}' non trouvee.")
        return False
    
    def nombre_regles(self) -> int:
        """
        Retourne le nombre de regles dans la base.
        
        Returns:
            Nombre de regles
        """
        return len(self.regles)
    
    def afficher_regles(self) -> None:
        """Affiche un resume de toutes les regles de la base."""
        print("\n" + "=" * 60)
        print("    BASE DE REGLES - SYSTEME EXPERT PRIX PC")
        print("=" * 60)
        print(f"\nNombre de regles : {self.nombre_regles()}\n")
        
        for i, regle in enumerate(self.regles, 1):
            prix_str = f"{regle['prix_min']} - {regle['prix_max']} euros"
            if regle['prix_max'] >= 10000:
                prix_str = f"> {regle['prix_min']} euros"
            
            print(f"{i}. {regle['nom']} ({prix_str})")
            print(f"   Description : {regle['description']}")
            print(f"   Confiance de base : {regle['confiance_base'] * 100:.0f}%")
            print()
        
        print("=" * 60)
