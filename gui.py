#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Graphique - Systeme Expert Prix PC Portable
======================================================

Ce module fournit une interface graphique (GUI) utilisant Tkinter
pour le systeme expert d'estimation de prix de PC portable.

Theme: Hacker / Cyberpunk / Futuriste

Auteur: TP Universitaire - Intelligence Artificielle
Date: Novembre 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import List, Tuple

# Importation des modules du systeme expert
from base_faits import BaseFaits
from base_regles import BaseRegles
from moteur_inference import MoteurInference


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
    Interface graphique pour le systeme expert d'estimation de prix PC.
    Theme Hacker / Cyberpunk avec effets futuristes.
    """
    
    def __init__(self):
        """Initialise l'interface graphique et les composants du systeme expert."""
        # Initialisation des composants du systeme expert
        self.base_faits = BaseFaits()
        self.base_regles = BaseRegles()
        self.moteur = MoteurInference(self.base_faits, self.base_regles)
        
        # Creation de la fenetre principale
        self.root = tk.Tk()
        self.root.title("[SYS_EXPERT] :: Prix PC Portable v2.0")
        self.root.geometry("1000x800")
        self.root.minsize(900, 700)
        self.root.configure(bg=COLORS["bg_dark"])
        
        # Configurer le style ttk pour le theme hacker
        self._configurer_style()
        
        # Variables pour les ComboBox
        self.variables = {}
        
        # Variables pour les Checkbuttons
        self.check_vars = {}
        
        # Construction de l'interface
        self._creer_interface()
        
        # Afficher l'avertissement au demarrage
        self._afficher_avertissement()
    
    def _configurer_style(self):
        """Configure le style ttk pour le theme hacker."""
        style = ttk.Style()
        
        # Configuration generale
        style.theme_use('clam')
        
        # Frame
        style.configure(
            "Hacker.TFrame",
            background=COLORS["bg_dark"]
        )
        
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
        
        # Button
        style.configure(
            "Hacker.TButton",
            background=COLORS["bg_button"],
            foreground=COLORS["text_primary"],
            font=("Consolas", 10, "bold"),
            bordercolor=COLORS["accent"],
            focuscolor=COLORS["accent"],
            padding=(15, 8)
        )
        style.map(
            "Hacker.TButton",
            background=[("active", COLORS["bg_button_hover"])],
            foreground=[("active", COLORS["text_cyan"])]
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
        style.map(
            "Hacker.TCombobox",
            fieldbackground=[("readonly", COLORS["bg_input"])],
            selectbackground=[("readonly", COLORS["accent"])]
        )
        
        # Checkbutton
        style.configure(
            "Hacker.TCheckbutton",
            background=COLORS["bg_panel"],
            foreground=COLORS["text_secondary"],
            font=("Consolas", 10),
            indicatorcolor=COLORS["bg_input"]
        )
        style.map(
            "Hacker.TCheckbutton",
            background=[("active", COLORS["bg_panel"])],
            foreground=[("active", COLORS["text_cyan"])]
        )
        
        # Separator
        style.configure(
            "Hacker.TSeparator",
            background=COLORS["accent"]
        )
    
    def _creer_interface(self):
        """Cree tous les elements de l'interface graphique."""
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
        
        # Banniere
        self._creer_banniere()
        
        # Section des specifications
        self._creer_section_specifications()
        
        # Section des options
        self._creer_section_options()
        
        # Boutons d'action
        self._creer_boutons()
        
        # Zone de resultats
        self._creer_zone_resultats()
        
        # Footer
        self._creer_footer()
    
    def _creer_banniere(self):
        """Cree la banniere ASCII art style hacker."""
        banner_frame = tk.Frame(self.scrollable_frame, bg=COLORS["bg_dark"])
        banner_frame.pack(fill="x", padx=10, pady=10)
        
        # Banniere ASCII art cyberpunk
        banner = """
    ╔══════════════════════════════════════════════════════════════════════════════════════╗
    ║  ░██████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗███████╗                        ║
    ║  ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝                        ║
    ║  ╚█████╗  ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║█████╗                          ║
    ║   ╚═══██╗  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══╝                          ║
    ║  ██████╔╝   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║███████╗                        ║
    ║  ╚═════╝    ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝                        ║
    ║                                                                                      ║
    ║  ███████╗██╗  ██╗██████╗ ███████╗██████╗ ████████╗     █████╗ ██╗                     ║
    ║  ██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝    ██╔══██╗██║                     ║
    ║  █████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝   ██║       ███████║██║                     ║
    ║  ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗   ██║       ██╔══██║██║                     ║
    ║  ███████╗██╔╝ ██╗██║     ███████╗██║  ██║   ██║       ██║  ██║██║                     ║
    ║  ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝                     ║
    ║                                                                                      ║
    ║  ┌─────────────────────────────────────────────────────────────────────────────────┐ ║
    ║  │  [SYSTEM]  ESTIMATION PRIX PC PORTABLE  ::  FORWARD CHAINING ENGINE v2.0       │ ║
    ║  │  [STATUS]  ONLINE  ::  READY FOR INPUT  ::  AI INFERENCE MODULE LOADED         │ ║
    ║  └─────────────────────────────────────────────────────────────────────────────────┘ ║
    ╚══════════════════════════════════════════════════════════════════════════════════════╝
"""
        
        # Container avec bordure
        container = tk.Frame(banner_frame, bg=COLORS["accent"], padx=2, pady=2)
        container.pack(fill="x", pady=5)
        
        inner_frame = tk.Frame(container, bg=COLORS["bg_dark"])
        inner_frame.pack(fill="x")
        
        # Label pour la banniere
        banner_label = tk.Label(
            inner_frame,
            text=banner,
            font=("Consolas", 7),
            fg=COLORS["text_primary"],
            bg=COLORS["bg_dark"],
            justify="left"
        )
        banner_label.pack(padx=5, pady=5)
        
        # Barre de status animee
        status_frame = tk.Frame(self.scrollable_frame, bg=COLORS["bg_panel"])
        status_frame.pack(fill="x", padx=12, pady=(0, 10))
        
        status_text = "[>>] TERMINAL READY  |  [>>] BASE DE REGLES: 8 RULES LOADED  |  [>>] INFERENCE ENGINE: ACTIVE"
        status_label = tk.Label(
            status_frame,
            text=status_text,
            font=("Consolas", 9),
            fg=COLORS["text_cyan"],
            bg=COLORS["bg_panel"]
        )
        status_label.pack(pady=5)
    
    def _creer_section_specifications(self):
        """Cree la section des specifications principales."""
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
        
        # Grille des specifications
        grid_frame = tk.Frame(specs_frame, bg=COLORS["bg_panel"])
        grid_frame.pack(fill="x")
        
        # Liste des specifications avec leurs options
        specifications = [
            ("SCREEN_SIZE", "taille_ecran", self.base_faits.options_taille_ecran),
            ("USAGE_TYPE", "usage", self.base_faits.options_usage),
            ("CPU_MODEL", "processeur", self.base_faits.options_processeur),
            ("CPU_GEN", "generation_cpu", self.base_faits.options_generation_cpu),
            ("RAM_SIZE", "ram", self.base_faits.options_ram),
            ("STORAGE", "stockage", self.base_faits.options_stockage),
            ("GPU_TYPE", "carte_graphique", self.base_faits.options_carte_graphique),
            ("DISPLAY_RES", "ecran", self.base_faits.options_ecran),
            ("REFRESH_RATE", "taux_rafraichissement", self.base_faits.options_taux_rafraichissement),
            ("BRAND", "marque", self.base_faits.options_marque),
            ("WEIGHT", "poids", self.base_faits.options_poids),
        ]
        
        # Creer les widgets en 2 colonnes
        for i, (label_text, var_name, options) in enumerate(specifications):
            row = i // 2
            col = (i % 2) * 2
            
            # Container pour chaque input
            input_container = tk.Frame(grid_frame, bg=COLORS["bg_panel"])
            input_container.grid(row=row, column=col, sticky="ew", padx=10, pady=8)
            grid_frame.columnconfigure(col, weight=1)
            
            # Label avec prefixe style terminal
            label = tk.Label(
                input_container,
                text=f">{label_text}:",
                font=("Consolas", 10, "bold"),
                fg=COLORS["text_secondary"],
                bg=COLORS["bg_panel"]
            )
            label.pack(anchor="w")
            
            # ComboBox avec style
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
            combo.current(0)
            
            # Configuration du style de la combobox
            combo.option_add('*TCombobox*Listbox.background', COLORS["bg_input"])
            combo.option_add('*TCombobox*Listbox.foreground', COLORS["text_primary"])
            combo.option_add('*TCombobox*Listbox.selectBackground', COLORS["accent"])
            combo.option_add('*TCombobox*Listbox.selectForeground', COLORS["bg_dark"])
    
    def _creer_section_options(self):
        """Cree la section des options supplementaires (checkboxes)."""
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
        
        # Liste des options booleennes
        options_bool = [
            ("NUMPAD", "pave_numerique"),
            ("BACKLIT_KB", "clavier_retroeclaire"),
            ("RGB_KEYBOARD", "clavier_rgb"),
            ("THUNDERBOLT", "thunderbolt"),
            ("HD_WEBCAM", "webcam_hd"),
            ("FINGERPRINT", "lecteur_empreinte"),
        ]
        
        # Creer les checkbuttons en 3 colonnes
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
        """Cree les boutons d'action."""
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
        
        # Bouton Reinitialiser - Jaune
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
        
        # Bouton Afficher les regles - Cyan
        btn_regles = tk.Button(
            boutons_frame,
            text="[ VIEW RULES ]",
            bg=COLORS["text_cyan"],
            fg=COLORS["bg_dark"],
            activebackground="#00cccc",
            activeforeground=COLORS["bg_dark"],
            command=self._afficher_regles,
            **btn_config
        )
        btn_regles.pack(side="left", padx=5)
        
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
        """Cree la zone d'affichage des resultats."""
        # Container avec bordure
        container = tk.Frame(self.scrollable_frame, bg=COLORS["text_primary"], padx=2, pady=2)
        container.pack(fill="both", expand=True, padx=10, pady=5)
        
        resultats_frame = tk.Frame(container, bg=COLORS["bg_panel"], padx=10, pady=10)
        resultats_frame.pack(fill="both", expand=True)
        
        # Titre de section
        title_label = tk.Label(
            resultats_frame,
            text="[ OUTPUT TERMINAL :: ANALYSIS RESULTS ]",
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
║                    SYSTEME EXPERT :: TERMINAL                        ║
╚══════════════════════════════════════════════════════════════════════╝

[SYSTEM] Initialisation complete...
[STATUS] En attente des specifications...

> Selectionnez les caracteristiques du PC portable
> Cliquez sur [ EXECUTE ANALYSIS ] pour lancer l'estimation

[READY] Systeme pret pour l'analyse_
"""
        self.resultats_text.insert(tk.END, welcome_msg, "green")
        self.resultats_text.config(state=tk.DISABLED)
    
    def _creer_footer(self):
        """Cree le footer."""
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
            text="[SYS_EXPERT v2.0] :: TP Universitaire - Intelligence Artificielle :: 2025",
            font=("Consolas", 9),
            fg=COLORS["text_gray"],
            bg=COLORS["bg_dark"]
        )
        credit_label.pack()
    
    def _afficher_avertissement(self):
        """Affiche l'avertissement au demarrage."""
        # Creer une fenetre personnalisee pour l'avertissement
        warn_window = tk.Toplevel(self.root)
        warn_window.title("[WARNING]")
        warn_window.geometry("500x350")
        warn_window.configure(bg=COLORS["bg_dark"])
        warn_window.resizable(False, False)
        warn_window.transient(self.root)
        warn_window.grab_set()
        
        # Centrer la fenetre
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

[WARNING] Ce systeme expert est UNIQUEMENT
          a but EDUCATIF et PEDAGOGIQUE.

[INFO] Les estimations de prix sont INDICATIVES
       et peuvent varier selon :

       > Les promotions et offres en cours
       > La disponibilite des produits
       > Le marche et la region d'achat
       > Les configurations exactes

[NOTICE] Consultez les sites marchands
         pour des prix reels.

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
    
    def _collecter_specifications(self):
        """Collecte les specifications depuis l'interface graphique."""
        self.base_faits.reinitialiser()
        
        for var_name, var in self.variables.items():
            self.base_faits.ajouter_fait(var_name, var.get())
        
        for var_name, var in self.check_vars.items():
            self.base_faits.ajouter_fait(var_name, var.get())
    
    def _lancer_estimation(self):
        """Lance l'estimation de prix."""
        self._collecter_specifications()
        estimations = self.moteur.inferer()
        self._afficher_resultats(estimations)
    
    def _afficher_resultats(self, estimations: List[Tuple[str, float, str, int, int]]):
        """Affiche les resultats de l'estimation avec style futuriste."""
        self.resultats_text.config(state=tk.NORMAL)
        self.resultats_text.delete(1.0, tk.END)
        
        # En-tete
        header = """
╔══════════════════════════════════════════════════════════════════════╗
║              ANALYSIS COMPLETE :: RESULTS OUTPUT                     ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        self.resultats_text.insert(tk.END, header, "header")
        
        self.resultats_text.insert(tk.END, "\n[PROCESSING] Analyse des specifications...\n", "cyan")
        self.resultats_text.insert(tk.END, "[INFERENCE] Moteur de chainage avant active...\n", "cyan")
        self.resultats_text.insert(tk.END, "[MATCHING] Comparaison avec la base de regles...\n\n", "cyan")
        
        if not estimations:
            self.resultats_text.insert(tk.END, "╔════════════════════════════════════════════════════════════════╗\n", "red")
            self.resultats_text.insert(tk.END, "║  [ERROR] AUCUNE CORRESPONDANCE TROUVEE                        ║\n", "red")
            self.resultats_text.insert(tk.END, "╚════════════════════════════════════════════════════════════════╝\n\n", "red")
            self.resultats_text.insert(tk.END, "[ANALYSIS] Causes possibles:\n", "yellow")
            self.resultats_text.insert(tk.END, "  > Specifications inhabituelles\n", "gray")
            self.resultats_text.insert(tk.END, "  > Combinaison de composants atypique\n", "gray")
            self.resultats_text.insert(tk.END, "  > Base de regles incomplete\n\n", "gray")
            self.resultats_text.insert(tk.END, "[SUGGEST] Consultez les sites marchands directement.\n", "yellow")
        else:
            nb_resultats = min(3, len(estimations))
            self.resultats_text.insert(tk.END, f"[SUCCESS] {nb_resultats} ESTIMATION(S) TROUVEE(S)\n\n", "green")
            
            for i, (nom, confiance, description, prix_min, prix_max) in enumerate(estimations[:nb_resultats], 1):
                pourcentage = confiance * 100
                
                # Determiner la couleur selon la confiance
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
                if prix_max >= 10000:
                    prix_str = f"> {prix_min} EUR"
                else:
                    prix_str = f"{prix_min} - {prix_max} EUR"
                
                # Affichage du resultat
                self.resultats_text.insert(tk.END, f"┌──────────────────────────────────────────────────────────────┐\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  RESULT #{i}: ", "white")
                self.resultats_text.insert(tk.END, f"{nom.upper()}\n", conf_color)
                self.resultats_text.insert(tk.END, f"├──────────────────────────────────────────────────────────────┤\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  [PRICE RANGE]  ", "gray")
                self.resultats_text.insert(tk.END, f"{prix_str}\n", "white")
                self.resultats_text.insert(tk.END, f"│  [CONFIDENCE]   ", "gray")
                self.resultats_text.insert(tk.END, f"{pourcentage:.1f}% ", conf_color)
                self.resultats_text.insert(tk.END, f"[{level}]\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  [INDICATOR]    ", "gray")
                self.resultats_text.insert(tk.END, f"{indicator}\n", conf_color)
                self.resultats_text.insert(tk.END, f"│  [INFO]         ", "gray")
                self.resultats_text.insert(tk.END, f"{description}\n", "white")
                self.resultats_text.insert(tk.END, f"└──────────────────────────────────────────────────────────────┘\n\n", conf_color)
        
        # Footer
        self.resultats_text.insert(tk.END, "═" * 70 + "\n", "gray")
        self.resultats_text.insert(tk.END, "[NOTICE] Cette estimation est INDICATIVE uniquement.\n", "yellow")
        self.resultats_text.insert(tk.END, "[END] Analyse terminee_\n", "green")
        
        self.resultats_text.config(state=tk.DISABLED)
    
    def _reinitialiser(self):
        """Reinitialise le formulaire."""
        # Remettre les ComboBox a la premiere valeur
        for var_name, var in self.variables.items():
            options = getattr(self.base_faits, f"options_{var_name}", None)
            if options:
                var.set(options[0])
        
        # Decocher toutes les checkboxes
        for var in self.check_vars.values():
            var.set(False)
        
        # Reinitialiser la base de faits
        self.base_faits.reinitialiser()
        
        # Afficher message de reset
        self.resultats_text.config(state=tk.NORMAL)
        self.resultats_text.delete(1.0, tk.END)
        
        reset_msg = """
╔══════════════════════════════════════════════════════════════════════╗
║                    SYSTEM RESET COMPLETE                             ║
╚══════════════════════════════════════════════════════════════════════╝

[RESET] Tous les parametres ont ete reinitialises...
[STATUS] Base de faits videe...
[STATUS] Interface remise a zero...

[READY] Systeme pret pour une nouvelle analyse_
"""
        self.resultats_text.insert(tk.END, reset_msg, "yellow")
        self.resultats_text.config(state=tk.DISABLED)
    
    def _afficher_regles(self):
        """Affiche les regles dans une nouvelle fenetre."""
        regles_window = tk.Toplevel(self.root)
        regles_window.title("[RULES DATABASE]")
        regles_window.geometry("750x550")
        regles_window.configure(bg=COLORS["bg_dark"])
        
        # Container
        container = tk.Frame(regles_window, bg=COLORS["accent"], padx=2, pady=2)
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        inner = tk.Frame(container, bg=COLORS["bg_dark"])
        inner.pack(fill="both", expand=True)
        
        # Zone de texte
        text_area = tk.Text(
            inner,
            font=("Consolas", 10),
            bg=COLORS["bg_dark"],
            fg=COLORS["text_primary"],
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        text_area.pack(fill="both", expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_area, command=text_area.yview)
        scrollbar.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scrollbar.set)
        
        # Afficher les regles
        header = """
╔══════════════════════════════════════════════════════════════════════╗
║                   RULES DATABASE :: SYSTEME EXPERT                   ║
╚══════════════════════════════════════════════════════════════════════╝
"""
        text_area.insert(tk.END, header)
        text_area.insert(tk.END, f"\n[INFO] Nombre de regles chargees: {self.base_regles.nombre_regles()}\n\n")
        
        for i, regle in enumerate(self.base_regles.obtenir_regles(), 1):
            prix_str = f"{regle['prix_min']} - {regle['prix_max']} EUR"
            if regle['prix_max'] >= 10000:
                prix_str = f"> {regle['prix_min']} EUR"
            
            text_area.insert(tk.END, f"┌─────────────────────────────────────────────────────────────┐\n")
            text_area.insert(tk.END, f"│ RULE #{i}: {regle['nom'].upper()}\n")
            text_area.insert(tk.END, f"├─────────────────────────────────────────────────────────────┤\n")
            text_area.insert(tk.END, f"│ [PRICE]      {prix_str}\n")
            text_area.insert(tk.END, f"│ [CONFIDENCE] {regle['confiance_base'] * 100:.0f}%\n")
            text_area.insert(tk.END, f"│ [DESC]       {regle['description']}\n")
            text_area.insert(tk.END, f"└─────────────────────────────────────────────────────────────┘\n\n")
        
        text_area.config(state=tk.DISABLED)
    
    def _afficher_aide(self):
        """Affiche l'aide."""
        aide_window = tk.Toplevel(self.root)
        aide_window.title("[HELP TERMINAL]")
        aide_window.geometry("600x500")
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

[USAGE] Comment utiliser le systeme:

  1. Selectionnez les specifications dans les menus deroulants
  2. Cochez les options supplementaires si presentes
  3. Cliquez sur [ EXECUTE ANALYSIS ]
  4. Les resultats s'affichent dans le terminal

[LEGEND] Interpretation des resultats:

  > HIGH   (80-100%) : Forte probabilite - Fiable
  > MEDIUM (60-80%)  : Probabilite moyenne
  > LOW    (<60%)    : Faible probabilite

[BUTTONS] Actions disponibles:

  > [ EXECUTE ANALYSIS ] : Lance l'estimation
  > [ RESET SYSTEM ]     : Reinitialise le formulaire
  > [ VIEW RULES ]       : Affiche la base de regles
  > [ HELP ]             : Affiche cette aide

[WARNING] Ce systeme est a but educatif uniquement.
          Les prix sont indicatifs et variables.

╔══════════════════════════════════════════════════════════════╗
║  [SYS_EXPERT v2.0] :: Forward Chaining Inference Engine     ║
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
# POINT D'ENTREE
# ============================================================

if __name__ == "__main__":
    app = SystemeExpertGUI()
    app.executer()
