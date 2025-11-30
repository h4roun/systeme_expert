#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Graphique - Système Expert Prix PC Portable (Experta)
================================================================

Ce module fournit une interface graphique (GUI) utilisant Tkinter
pour le système expert d'estimation de prix de PC portable.

Utilise la bibliothèque Experta pour le moteur d'inférence.

Theme: Hacker / Cyberpunk / Futuriste

Auteur: TP Universitaire - Intelligence Artificielle
Date: Novembre 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict

# Importation des modules du système expert
from faits import SpecificationPC, OPTIONS, OPTIONS_BOOLEENNES, obtenir_options
from regles import SystemeExpertPrixPC


# ============================================================
# THEME HACKER - COULEURS
# ============================================================
COLORS = {
    "bg_dark": "#0a0a0a",
    "bg_panel": "#0d1117",
    "bg_input": "#161b22",
    "bg_button": "#21262d",
    "bg_button_hover": "#30363d",
    "text_primary": "#00ff00",
    "text_secondary": "#39ff14",
    "text_cyan": "#00ffff",
    "text_yellow": "#ffff00",
    "text_orange": "#ff6600",
    "text_red": "#ff0040",
    "text_white": "#e6edf3",
    "text_gray": "#8b949e",
    "border": "#30363d",
    "accent": "#00ff00",
    "accent_cyan": "#00ffff",
}


class SystemeExpertGUI:
    """
    Interface graphique pour le système expert d'estimation de prix PC.
    Utilise Experta pour l'inférence.
    Theme Hacker / Cyberpunk avec effets futuristes.
    """
    
    def __init__(self):
        """Initialise l'interface graphique et les composants du système expert."""
        # Création de la fenêtre principale
        self.root = tk.Tk()
        self.root.title("[SYS_EXPERT] :: Prix PC Portable v2.0 - EXPERTA")
        self.root.geometry("1000x800")
        self.root.minsize(900, 700)
        self.root.configure(bg=COLORS["bg_dark"])
        
        # Variables pour les ComboBox
        self.variables = {}
        
        # Variables pour les Checkbuttons
        self.check_vars = {}
        
        # Configurer le style ttk
        self._configurer_style()
        
        # Construction de l'interface
        self._creer_interface()
        
        # Afficher l'avertissement au démarrage
        self._afficher_avertissement()
    
    def _configurer_style(self):
        """Configure le style ttk pour le thème hacker."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame
        style.configure("Hacker.TFrame", background=COLORS["bg_dark"])
        
        # LabelFrame
        style.configure(
            "Hacker.TLabelframe",
            background=COLORS["bg_panel"],
            foreground=COLORS["text_primary"],
            bordercolor=COLORS["accent"],
            relief="solid"
        )
        style.configure(
            "Hacker.TLabelframe.Label",
            background=COLORS["bg_panel"],
            foreground=COLORS["text_cyan"],
            font=("Consolas", 11, "bold")
        )
        
        # Label
        style.configure(
            "Hacker.TLabel",
            background=COLORS["bg_panel"],
            foreground=COLORS["text_primary"],
            font=("Consolas", 10)
        )
        
        # Combobox
        style.configure(
            "Hacker.TCombobox",
            background=COLORS["bg_input"],
            foreground=COLORS["text_primary"],
            fieldbackground=COLORS["bg_input"],
            selectbackground=COLORS["accent"],
            selectforeground=COLORS["bg_dark"],
            arrowcolor=COLORS["text_primary"],
            font=("Consolas", 9)
        )
    
    def _creer_interface(self):
        """Crée tous les éléments de l'interface graphique."""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=COLORS["bg_dark"])
        main_frame.pack(fill="both", expand=True)
        
        # Canvas avec scrollbar
        self.canvas = tk.Canvas(main_frame, bg=COLORS["bg_dark"], highlightthickness=0)
        scrollbar = tk.Scrollbar(
            main_frame,
            orient="vertical",
            command=self.canvas.yview,
            bg=COLORS["bg_panel"],
            troughcolor=COLORS["bg_dark"],
            activebackground=COLORS["accent"]
        )
        
        self.scrollable_frame = tk.Frame(self.canvas, bg=COLORS["bg_dark"])
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Binding pour le scroll avec la molette
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Bannière
        self._creer_banniere()
        
        # Section des spécifications
        self._creer_section_specifications()
        
        # Section des options
        self._creer_section_options()
        
        # Boutons d'action
        self._creer_boutons()
        
        # Zone de résultats
        self._creer_zone_resultats()
        
        # Footer
        self._creer_footer()
    
    def _creer_banniere(self):
        """Crée la bannière ASCII art style hacker."""
        banner_frame = tk.Frame(self.scrollable_frame, bg=COLORS["bg_dark"])
        banner_frame.pack(fill="x", padx=10, pady=10)
        
        # Bannière ASCII art cyberpunk
        banner = """
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
        
        # Container avec bordure
        container = tk.Frame(banner_frame, bg=COLORS["accent"], padx=2, pady=2)
        container.pack(fill="x", pady=5)
        
        inner_frame = tk.Frame(container, bg=COLORS["bg_dark"])
        inner_frame.pack(fill="x")
        
        # Label pour la bannière
        banner_label = tk.Label(
            inner_frame,
            text=banner,
            font=("Consolas", 7),
            fg=COLORS["text_primary"],
            bg=COLORS["bg_dark"],
            justify="left"
        )
        banner_label.pack(padx=5, pady=5)
        
        # Barre de status
        status_frame = tk.Frame(self.scrollable_frame, bg=COLORS["bg_panel"])
        status_frame.pack(fill="x", padx=12, pady=(0, 10))
        
        status_text = "[>>] EXPERTA READY  |  [>>] RETE ALGORITHM ACTIVE  |  [>>] KNOWLEDGE ENGINE: LOADED"
        status_label = tk.Label(
            status_frame,
            text=status_text,
            font=("Consolas", 9),
            fg=COLORS["text_cyan"],
            bg=COLORS["bg_panel"]
        )
        status_label.pack(pady=5)
    
    def _creer_section_specifications(self):
        """Crée la section des spécifications principales."""
        # Container avec bordure verte
        container = tk.Frame(self.scrollable_frame, bg=COLORS["accent"], padx=1, pady=1)
        container.pack(fill="x", padx=10, pady=5)
        
        specs_frame = tk.Frame(container, bg=COLORS["bg_panel"], padx=15, pady=15)
        specs_frame.pack(fill="x")
        
        # Titre de section
        title_frame = tk.Frame(specs_frame, bg=COLORS["bg_panel"])
        title_frame.pack(fill="x", pady=(0, 15))
        
        title_label = tk.Label(
            title_frame,
            text="[ HARDWARE SPECIFICATIONS INPUT ]",
            font=("Consolas", 12, "bold"),
            fg=COLORS["text_cyan"],
            bg=COLORS["bg_panel"]
        )
        title_label.pack(anchor="w")
        
        # Grille des spécifications
        grid_frame = tk.Frame(specs_frame, bg=COLORS["bg_panel"])
        grid_frame.pack(fill="x")
        
        # Liste des spécifications
        specifications = [
            ("SCREEN_SIZE", "taille_ecran"),
            ("USAGE_TYPE", "usage"),
            ("CPU_MODEL", "processeur"),
            ("CPU_GEN", "generation_cpu"),
            ("RAM_SIZE", "ram"),
            ("STORAGE", "stockage"),
            ("GPU_TYPE", "carte_graphique"),
            ("DISPLAY_RES", "ecran"),
            ("REFRESH_RATE", "taux_rafraichissement"),
            ("BRAND", "marque"),
            ("WEIGHT", "poids"),
        ]
        
        # Créer les widgets en 2 colonnes
        for i, (label_text, var_name) in enumerate(specifications):
            row = i // 2
            col = (i % 2) * 2
            
            # Container pour chaque input
            input_container = tk.Frame(grid_frame, bg=COLORS["bg_panel"])
            input_container.grid(row=row, column=col, sticky="ew", padx=10, pady=8)
            grid_frame.columnconfigure(col, weight=1)
            
            # Label avec préfixe style terminal
            label = tk.Label(
                input_container,
                text=f">{label_text}:",
                font=("Consolas", 10, "bold"),
                fg=COLORS["text_secondary"],
                bg=COLORS["bg_panel"]
            )
            label.pack(anchor="w")
            
            # ComboBox
            options = obtenir_options(var_name)
            self.variables[var_name] = tk.StringVar()
            combo = ttk.Combobox(
                input_container,
                textvariable=self.variables[var_name],
                values=options,
                state="readonly",
                width=38,
                font=("Consolas", 9)
            )
            combo.pack(anchor="w", pady=(3, 0))
            if options:
                combo.current(0)
            
            # Style de la combobox
            combo.option_add('*TCombobox*Listbox.background', COLORS["bg_input"])
            combo.option_add('*TCombobox*Listbox.foreground', COLORS["text_primary"])
            combo.option_add('*TCombobox*Listbox.selectBackground', COLORS["accent"])
            combo.option_add('*TCombobox*Listbox.selectForeground', COLORS["bg_dark"])
    
    def _creer_section_options(self):
        """Crée la section des options supplémentaires (checkboxes)."""
        # Container avec bordure cyan
        container = tk.Frame(self.scrollable_frame, bg=COLORS["accent_cyan"], padx=1, pady=1)
        container.pack(fill="x", padx=10, pady=5)
        
        options_frame = tk.Frame(container, bg=COLORS["bg_panel"], padx=15, pady=15)
        options_frame.pack(fill="x")
        
        # Titre de section
        title_label = tk.Label(
            options_frame,
            text="[ ADDITIONAL FEATURES ]",
            font=("Consolas", 12, "bold"),
            fg=COLORS["text_yellow"],
            bg=COLORS["bg_panel"]
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Frame pour les checkboxes
        check_frame = tk.Frame(options_frame, bg=COLORS["bg_panel"])
        check_frame.pack(fill="x")
        
        # Liste des options booléennes
        options_bool = [
            ("NUMPAD", "pave_numerique"),
            ("BACKLIT_KB", "clavier_retroeclaire"),
            ("RGB_KEYBOARD", "clavier_rgb"),
            ("THUNDERBOLT", "thunderbolt"),
            ("HD_WEBCAM", "webcam_hd"),
            ("FINGERPRINT", "lecteur_empreinte"),
        ]
        
        # Créer les checkbuttons en 3 colonnes
        for i, (label_text, var_name) in enumerate(options_bool):
            row = i // 3
            col = i % 3
            
            self.check_vars[var_name] = tk.BooleanVar(value=False)
            
            check = tk.Checkbutton(
                check_frame,
                text=f"[{label_text}]",
                variable=self.check_vars[var_name],
                font=("Consolas", 10),
                fg=COLORS["text_secondary"],
                bg=COLORS["bg_panel"],
                selectcolor=COLORS["bg_input"],
                activebackground=COLORS["bg_panel"],
                activeforeground=COLORS["text_cyan"],
                highlightthickness=0,
                bd=0
            )
            check.grid(row=row, column=col, sticky="w", padx=15, pady=5)
    
    def _creer_boutons(self):
        """Crée les boutons d'action."""
        boutons_frame = tk.Frame(self.scrollable_frame, bg=COLORS["bg_dark"])
        boutons_frame.pack(fill="x", padx=10, pady=15)
        
        # Style des boutons
        btn_config = {
            "font": ("Consolas", 11, "bold"),
            "bd": 0,
            "padx": 20,
            "pady": 10,
            "cursor": "hand2"
        }
        
        # Bouton Estimer - Vert
        btn_estimer = tk.Button(
            boutons_frame,
            text="[ EXECUTE ANALYSIS ]",
            bg=COLORS["accent"],
            fg=COLORS["bg_dark"],
            activebackground=COLORS["text_secondary"],
            activeforeground=COLORS["bg_dark"],
            command=self._lancer_estimation,
            **btn_config
        )
        btn_estimer.pack(side="left", padx=5)
        
        # Bouton Réinitialiser - Jaune
        btn_reset = tk.Button(
            boutons_frame,
            text="[ RESET SYSTEM ]",
            bg=COLORS["text_yellow"],
            fg=COLORS["bg_dark"],
            activebackground="#cccc00",
            activeforeground=COLORS["bg_dark"],
            command=self._reinitialiser,
            **btn_config
        )
        btn_reset.pack(side="left", padx=5)
        
        # Bouton Test - Cyan
        btn_test = tk.Button(
            boutons_frame,
            text="[ RUN TEST ]",
            bg=COLORS["text_cyan"],
            fg=COLORS["bg_dark"],
            activebackground="#00cccc",
            activeforeground=COLORS["bg_dark"],
            command=self._lancer_test,
            **btn_config
        )
        btn_test.pack(side="left", padx=5)
        
        # Bouton Aide - Orange
        btn_aide = tk.Button(
            boutons_frame,
            text="[ HELP ]",
            bg=COLORS["text_orange"],
            fg=COLORS["bg_dark"],
            activebackground="#cc5500",
            activeforeground=COLORS["bg_dark"],
            command=self._afficher_aide,
            **btn_config
        )
        btn_aide.pack(side="left", padx=5)
    
    def _creer_zone_resultats(self):
        """Crée la zone d'affichage des résultats."""
        # Container avec bordure
        container = tk.Frame(self.scrollable_frame, bg=COLORS["text_primary"], padx=2, pady=2)
        container.pack(fill="both", expand=True, padx=10, pady=5)
        
        resultats_frame = tk.Frame(container, bg=COLORS["bg_panel"], padx=10, pady=10)
        resultats_frame.pack(fill="both", expand=True)
        
        # Titre de section
        title_label = tk.Label(
            resultats_frame,
            text="[ OUTPUT TERMINAL :: EXPERTA INFERENCE RESULTS ]",
            font=("Consolas", 12, "bold"),
            fg=COLORS["text_primary"],
            bg=COLORS["bg_panel"]
        )
        title_label.pack(anchor="w", pady=(0, 10))
        
        # Zone de texte avec style terminal
        self.resultats_text = tk.Text(
            resultats_frame,
            height=15,
            font=("Consolas", 10),
            bg=COLORS["bg_dark"],
            fg=COLORS["text_primary"],
            insertbackground=COLORS["text_primary"],
            selectbackground=COLORS["accent"],
            selectforeground=COLORS["bg_dark"],
            bd=0,
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.resultats_text.pack(fill="both", expand=True)
        
        # Configurer les tags pour les couleurs
        self.resultats_text.tag_configure("green", foreground=COLORS["text_primary"])
        self.resultats_text.tag_configure("cyan", foreground=COLORS["text_cyan"])
        self.resultats_text.tag_configure("yellow", foreground=COLORS["text_yellow"])
        self.resultats_text.tag_configure("orange", foreground=COLORS["text_orange"])
        self.resultats_text.tag_configure("red", foreground=COLORS["text_red"])
        self.resultats_text.tag_configure("white", foreground=COLORS["text_white"])
        self.resultats_text.tag_configure("gray", foreground=COLORS["text_gray"])
        self.resultats_text.tag_configure("bold", font=("Consolas", 10, "bold"))
        self.resultats_text.tag_configure("header", font=("Consolas", 11, "bold"), foreground=COLORS["text_cyan"])
        
        # Message initial
        self._afficher_message_initial()
    
    def _afficher_message_initial(self):
        """Affiche le message initial dans le terminal."""
        self.resultats_text.config(state=tk.NORMAL)
        self.resultats_text.delete(1.0, tk.END)
        
        welcome_msg = """
╔══════════════════════════════════════════════════════════════════════╗
║                 EXPERTA EXPERT SYSTEM :: TERMINAL                    ║
╚══════════════════════════════════════════════════════════════════════╝

[SYSTEM] Experta Knowledge Engine initialisé...
[RETE] Algorithme RETE prêt pour le pattern matching...
[STATUS] En attente des spécifications...

> Sélectionnez les caractéristiques du PC portable
> Cliquez sur [ EXECUTE ANALYSIS ] pour lancer l'inférence

[READY] Système prêt pour l'analyse_
"""
        self.resultats_text.insert(tk.END, welcome_msg, "green")
        self.resultats_text.config(state=tk.DISABLED)
    
    def _creer_footer(self):
        """Crée le footer."""
        footer_frame = tk.Frame(self.scrollable_frame, bg=COLORS["bg_dark"])
        footer_frame.pack(fill="x", padx=10, pady=10)
        
        footer_text = "═══════════════════════════════════════════════════════════════════════════════════════"
        footer_label = tk.Label(
            footer_frame,
            text=footer_text,
            font=("Consolas", 8),
            fg=COLORS["text_gray"],
            bg=COLORS["bg_dark"]
        )
        footer_label.pack()
        
        credit_label = tk.Label(
            footer_frame,
            text="[SYS_EXPERT v2.0] :: EXPERTA Engine :: TP Universitaire - Intelligence Artificielle :: 2025",
            font=("Consolas", 9),
            fg=COLORS["text_gray"],
            bg=COLORS["bg_dark"]
        )
        credit_label.pack()
    
    def _afficher_avertissement(self):
        """Affiche l'avertissement au démarrage."""
        warn_window = tk.Toplevel(self.root)
        warn_window.title("[WARNING]")
        warn_window.geometry("500x350")
        warn_window.configure(bg=COLORS["bg_dark"])
        warn_window.resizable(False, False)
        warn_window.transient(self.root)
        warn_window.grab_set()
        
        # Centrer la fenêtre
        warn_window.update_idletasks()
        x = (warn_window.winfo_screenwidth() - 500) // 2
        y = (warn_window.winfo_screenheight() - 350) // 2
        warn_window.geometry(f"+{x}+{y}")
        
        # Contenu
        container = tk.Frame(warn_window, bg=COLORS["text_yellow"], padx=2, pady=2)
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        inner = tk.Frame(container, bg=COLORS["bg_dark"])
        inner.pack(fill="both", expand=True)
        
        warning_text = """
╔═══════════════════════════════════════════════════╗
║           ⚠️  AVERTISSEMENT IMPORTANT  ⚠️          ║
╚═══════════════════════════════════════════════════╝

[WARNING] Ce système expert est UNIQUEMENT
          à but ÉDUCATIF et PÉDAGOGIQUE.

[INFO] Les estimations de prix sont INDICATIVES
       et peuvent varier selon :

       > Les promotions et offres en cours
       > La disponibilité des produits
       > Le marché et la région d'achat
       > Les configurations exactes

[ENGINE] Utilise la bibliothèque EXPERTA
         (inspirée de CLIPS)

"""
        
        text_label = tk.Label(
            inner,
            text=warning_text,
            font=("Consolas", 10),
            fg=COLORS["text_yellow"],
            bg=COLORS["bg_dark"],
            justify="left"
        )
        text_label.pack(pady=10)
        
        # Bouton OK
        btn_ok = tk.Button(
            inner,
            text="[ J'AI COMPRIS - CONTINUER ]",
            font=("Consolas", 11, "bold"),
            bg=COLORS["text_yellow"],
            fg=COLORS["bg_dark"],
            activebackground="#cccc00",
            command=warn_window.destroy,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        btn_ok.pack(pady=10)
    
    def _collecter_specifications(self) -> dict:
        """Collecte les spécifications depuis l'interface graphique."""
        specs = {}
        
        # Spécifications principales
        for var_name, var in self.variables.items():
            specs[var_name] = var.get()
        
        # Options booléennes
        for var_name, var in self.check_vars.items():
            specs[var_name] = var.get()
        
        return specs
    
    def _lancer_estimation(self):
        """Lance l'estimation de prix avec Experta."""
        specs = self._collecter_specifications()
        
        # Créer et exécuter le moteur Experta
        engine = SystemeExpertPrixPC()
        engine.reset()
        engine.declare(SpecificationPC(**specs))
        engine.run()
        
        # Récupérer et afficher les résultats
        estimations = engine.obtenir_estimations()
        self._afficher_resultats(estimations)
    
    def _lancer_test(self):
        """Lance un test avec des valeurs prédéfinies."""
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
        
        # Mettre à jour l'interface avec les valeurs de test
        for var_name, valeur in specs_test.items():
            if var_name in self.variables:
                self.variables[var_name].set(valeur)
            if var_name in self.check_vars:
                self.check_vars[var_name].set(valeur)
        
        # Créer et exécuter le moteur Experta
        engine = SystemeExpertPrixPC()
        engine.reset()
        engine.declare(SpecificationPC(**specs_test))
        engine.run()
        
        # Afficher les résultats
        estimations = engine.obtenir_estimations()
        self._afficher_resultats(estimations, test_mode=True)
    
    def _afficher_resultats(self, estimations: List[Dict], test_mode: bool = False):
        """Affiche les résultats de l'estimation avec style futuriste."""
        self.resultats_text.config(state=tk.NORMAL)
        self.resultats_text.delete(1.0, tk.END)
        
        # En-tête
        header = """
╔══════════════════════════════════════════════════════════════════════╗
║           EXPERTA INFERENCE COMPLETE :: RESULTS OUTPUT               ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        self.resultats_text.insert(tk.END, header, "header")
        
        if test_mode:
            self.resultats_text.insert(tk.END, "\n[MODE] Test avec valeurs prédéfinies (PC Gaming)\n", "yellow")
        
        self.resultats_text.insert(tk.END, "\n[EXPERTA] Moteur d'inférence exécuté...\n", "cyan")
        self.resultats_text.insert(tk.END, "[RETE] Pattern matching terminé...\n", "cyan")
        self.resultats_text.insert(tk.END, "[RULES] Évaluation des règles complète...\n\n", "cyan")
        
        if not estimations:
            self.resultats_text.insert(tk.END, "╔════════════════════════════════════════════════════════════════╗\n", "red")
            self.resultats_text.insert(tk.END, "║  [ERROR] AUCUNE CORRESPONDANCE TROUVÉE                        ║\n", "red")
            self.resultats_text.insert(tk.END, "╚════════════════════════════════════════════════════════════════╝\n\n", "red")
            self.resultats_text.insert(tk.END, "[ANALYSIS] Causes possibles:\n", "yellow")
            self.resultats_text.insert(tk.END, "  > Spécifications inhabituelles\n", "gray")
            self.resultats_text.insert(tk.END, "  > Combinaison de composants atypique\n", "gray")
            self.resultats_text.insert(tk.END, "  > Règles excluantes activées\n\n", "gray")
        else:
            nb_resultats = min(3, len(estimations))
            self.resultats_text.insert(tk.END, f"[SUCCESS] {nb_resultats} ESTIMATION(S) TROUVÉE(S)\n\n", "green")
            
            for i, est in enumerate(estimations[:nb_resultats], 1):
                pourcentage = est["confiance"] * 100
                
                # Déterminer la couleur selon la confiance
                if pourcentage >= 80:
                    conf_color = "green"
                    indicator = "████████████████████"
                    level = "HIGH"
                elif pourcentage >= 60:
                    conf_color = "yellow"
                    indicator = "████████████░░░░░░░░"
                    level = "MEDIUM"
                else:
                    conf_color = "orange"
                    indicator = "████████░░░░░░░░░░░░"
                    level = "LOW"
                
                # Formatage du prix
                if est["prix_max"] >= 10000:
                    prix_str = f"> {est['prix_min']} EUR"
                else:
                    prix_str = f"{est['prix_min']} - {est['prix_max']} EUR"
                
                # Affichage du résultat
                self.resultats_text.insert(tk.END, f"┌──────────────────────────────────────────────────────────────┐\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  RESULT #{i}: ", "white")
                self.resultats_text.insert(tk.END, f"{est['gamme'].upper()}\n", conf_color)
                self.resultats_text.insert(tk.END, f"├──────────────────────────────────────────────────────────────┤\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  [PRICE RANGE]  ", "gray")
                self.resultats_text.insert(tk.END, f"{prix_str}\n", "white")
                self.resultats_text.insert(tk.END, f"│  [CONFIDENCE]   ", "gray")
                self.resultats_text.insert(tk.END, f"{pourcentage:.1f}% ", conf_color)
                self.resultats_text.insert(tk.END, f"[{level}]\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  [INDICATOR]    ", "gray")
                self.resultats_text.insert(tk.END, f"{indicator}\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  [INFO]         ", "gray")
                self.resultats_text.insert(tk.END, f"{est['description']}\n", "white")
                self.resultats_text.insert(tk.END, f"└──────────────────────────────────────────────────────────────┘\n\n", conf_color)
        
        # Footer
        self.resultats_text.insert(tk.END, "═" * 70 + "\n", "gray")
        self.resultats_text.insert(tk.END, "[NOTICE] Cette estimation est INDICATIVE uniquement.\n", "yellow")
        self.resultats_text.insert(tk.END, "[ENGINE] Powered by EXPERTA (Python Expert System Library)\n", "cyan")
        self.resultats_text.insert(tk.END, "[END] Analyse terminée_\n", "green")
        
        self.resultats_text.config(state=tk.DISABLED)
    
    def _reinitialiser(self):
        """Réinitialise le formulaire."""
        # Remettre les ComboBox à la première valeur
        for var_name, var in self.variables.items():
            options = obtenir_options(var_name)
            if options:
                var.set(options[0])
        
        # Décocher toutes les checkboxes
        for var in self.check_vars.values():
            var.set(False)
        
        # Afficher message de reset
        self.resultats_text.config(state=tk.NORMAL)
        self.resultats_text.delete(1.0, tk.END)
        
        reset_msg = """
╔══════════════════════════════════════════════════════════════════════╗
║                    SYSTEM RESET COMPLETE                             ║
╚══════════════════════════════════════════════════════════════════════╝

[RESET] Tous les paramètres ont été réinitialisés...
[EXPERTA] Knowledge Engine prêt pour nouvelle inférence...
[STATUS] Interface remise à zéro...

[READY] Système prêt pour une nouvelle analyse_
"""
        self.resultats_text.insert(tk.END, reset_msg, "yellow")
        self.resultats_text.config(state=tk.DISABLED)
    
    def _afficher_aide(self):
        """Affiche l'aide."""
        aide_window = tk.Toplevel(self.root)
        aide_window.title("[HELP TERMINAL]")
        aide_window.geometry("600x550")
        aide_window.configure(bg=COLORS["bg_dark"])
        
        # Container
        container = tk.Frame(aide_window, bg=COLORS["text_cyan"], padx=2, pady=2)
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        inner = tk.Frame(container, bg=COLORS["bg_dark"])
        inner.pack(fill="both", expand=True)
        
        aide_text = """
╔══════════════════════════════════════════════════════════════╗
║                    HELP :: USER MANUAL                       ║
╚══════════════════════════════════════════════════════════════╝

[USAGE] Comment utiliser le système:

  1. Sélectionnez les spécifications dans les menus déroulants
  2. Cochez les options supplémentaires si présentes
  3. Cliquez sur [ EXECUTE ANALYSIS ]
  4. Les résultats s'affichent dans le terminal

[LEGEND] Interprétation des résultats:

  > HIGH   (80-100%) : Forte probabilité - Fiable
  > MEDIUM (60-80%)  : Probabilité moyenne
  > LOW    (<60%)    : Faible probabilité

[BUTTONS] Actions disponibles:

  > [ EXECUTE ANALYSIS ] : Lance l'inférence Experta
  > [ RESET SYSTEM ]     : Réinitialise le formulaire
  > [ RUN TEST ]         : Test avec valeurs prédéfinies
  > [ HELP ]             : Affiche cette aide

[EXPERTA] Bibliothèque utilisée:

  Experta est une bibliothèque Python pour construire
  des systèmes experts, inspirée de CLIPS.
  Elle utilise l'algorithme RETE pour le pattern matching.

╔══════════════════════════════════════════════════════════════╗
║  [SYS_EXPERT v2.0] :: EXPERTA Knowledge Engine              ║
╚══════════════════════════════════════════════════════════════╝
"""
        
        text_label = tk.Label(
            inner,
            text=aide_text,
            font=("Consolas", 10),
            fg=COLORS["text_cyan"],
            bg=COLORS["bg_dark"],
            justify="left"
        )
        text_label.pack(pady=10, padx=10)
    
    def executer(self):
        """Lance l'interface graphique."""
        self.root.mainloop()


# ============================================================
# POINT D'ENTRÉE
# ============================================================

if __name__ == "__main__":
    app = SystemeExpertGUI()
    app.executer()
