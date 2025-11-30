# 🖥️ Système Expert - Estimation de Prix de PC Portable

<div align="center">

```
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
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

**Système Expert d'Estimation de Prix de PC Portable**

*TP Universitaire - Intelligence Artificielle*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](#)

> 📌 **Cette branche contient l'implémentation manuelle.** Pour la version utilisant Experta (bibliothèque professionnelle), voir la branche [`experta`](../../tree/experta).

</div>

---

## 📋 Table des Matières

1. [Introduction](#-introduction)
2. [Architecture du Projet](#-architecture-du-projet)
3. [Concepts Théoriques](#-concepts-théoriques)
4. [Structure des Fichiers](#-structure-des-fichiers)
5. [Installation](#-installation)
6. [Utilisation](#-utilisation)
7. [Description des Modules](#-description-des-modules)
8. [Base de Règles](#-base-de-règles)
9. [Algorithme d'Inférence](#-algorithme-dinférence)
10. [Interface Graphique](#-interface-graphique)
11. [Exemples](#-exemples)
12. [Avertissement](#-avertissement)

---

## 🎯 Introduction

Ce projet implémente un **système expert** utilisant le **chaînage avant** (forward chaining) pour estimer la gamme de prix d'un ordinateur portable en fonction de ses spécifications techniques.

### Objectifs Pédagogiques

- Comprendre le fonctionnement d'un système expert
- Implémenter un moteur d'inférence en chaînage avant
- Manipuler des bases de faits et de règles
- Développer une interface graphique avec Tkinter

### Fonctionnalités

- ✅ Questionnaire interactif (console et GUI)
- ✅ 8 règles d'estimation de prix
- ✅ Calcul de score de confiance
- ✅ Interface graphique thème "Hacker"
- ✅ Architecture modulaire

---

## 🏗️ Architecture du Projet

```
systeme_expert/
│
├── 📄 main.py              # Point d'entrée console
├── 📄 gui.py               # Interface graphique Tkinter
├── 📄 base_faits.py        # Gestion des faits
├── 📄 base_regles.py       # Gestion des règles
├── 📄 moteur_inference.py  # Moteur d'inférence
└── 📄 README.md            # Documentation
```

### Diagramme de l'Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        INTERFACE UTILISATEUR                        │
│                    (main.py / gui.py)                               │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      SYSTEME EXPERT PRINCIPAL                        │
│                     (SystemeExpertPrixPC)                            │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │                    MOTEUR D'INFERENCE                           ││
│  │                  (moteur_inference.py)                          ││
│  │                                                                 ││
│  │    ┌──────────────────┐         ┌──────────────────┐           ││
│  │    │  BASE DE FAITS   │ ──────► │  BASE DE REGLES  │           ││
│  │    │ (base_faits.py)  │         │ (base_regles.py) │           ││
│  │    │                  │         │                  │           ││
│  │    │ • Spécifications │         │ • 8 règles       │           ││
│  │    │ • 11 critères    │         │ • Conditions     │           ││
│  │    │ • 6 options bool │         │ • Prix           │           ││
│  │    └──────────────────┘         └──────────────────┘           ││
│  │                      │                     │                    ││
│  │                      └──────────┬──────────┘                    ││
│  │                                 ▼                               ││
│  │                    ┌────────────────────────┐                   ││
│  │                    │   CHAÎNAGE AVANT       │                   ││
│  │                    │   (Forward Chaining)   │                   ││
│  │                    └────────────────────────┘                   ││
│  │                                 │                               ││
│  │                                 ▼                               ││
│  │                    ┌────────────────────────┐                   ││
│  │                    │   ESTIMATIONS + SCORES │                   ││
│  │                    │   DE CONFIANCE         │                   ││
│  │                    └────────────────────────┘                   ││
│  └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📚 Concepts Théoriques

### Qu'est-ce qu'un Système Expert ?

Un **système expert** est un programme informatique qui simule le raisonnement d'un expert humain dans un domaine spécifique. Il se compose de :

1. **Base de Faits** : Ensemble des informations connues sur le problème
2. **Base de Règles** : Ensemble des règles de décision (SI...ALORS...)
3. **Moteur d'Inférence** : Mécanisme qui applique les règles aux faits

### Chaînage Avant (Forward Chaining)

Le **chaînage avant** est une stratégie d'inférence qui :

1. Part des **faits connus** (données utilisateur)
2. Cherche les **règles applicables**
3. Déduit de **nouveaux faits** (conclusions)

```
FAITS CONNUS ──► RÈGLES ──► CONCLUSIONS

[Processeur: i7]      ┌─────────────────┐
[RAM: 16 Go]    ────► │ SI i7 ET 16Go   │ ────► [Prix: 1200-1800€]
[GPU: RTX 4060]       │ ET RTX          │       [Confiance: 85%]
                      │ ALORS Milieu/   │
                      │ Haut de gamme   │
                      └─────────────────┘
```

### Différence avec le Chaînage Arrière

| Chaînage Avant | Chaînage Arrière |
|----------------|------------------|
| Part des faits | Part des conclusions |
| Données → But | But → Données |
| "Que puis-je déduire ?" | "Comment prouver ce but ?" |
| Utilisé ici ✅ | Non utilisé |

---

## 📁 Structure des Fichiers

### 1. `base_faits.py` - Base de Faits

```python
class BaseFaits:
    """Gère la collecte et le stockage des spécifications PC."""
    
    # Attributs principaux
    faits: Dict[str, Any]           # Dictionnaire des spécifications
    options_processeur: List[str]   # Options disponibles
    options_ram: List[str]
    # ... autres options
    
    # Méthodes
    def collecter_faits()           # Questionnaire interactif
    def obtenir_fait(cle)           # Récupère un fait
    def ajouter_fait(cle, valeur)   # Ajoute/modifie un fait
    def reinitialiser()             # Vide les faits
```

### 2. `base_regles.py` - Base de Règles

```python
class BaseRegles:
    """Gère les règles d'estimation de prix."""
    
    # Structure d'une règle
    regle = {
        "nom": str,                      # Nom de la gamme
        "prix_min": int,                 # Prix minimum
        "prix_max": int,                 # Prix maximum
        "description": str,              # Description
        "conditions_requises": Dict,     # DOIVENT être satisfaites
        "conditions_optionnelles": Dict, # Bonus de confiance
        "conditions_excluantes": Dict,   # EXCLUENT la règle
        "confiance_base": float          # Score de base (0-1)
    }
    
    # Méthodes
    def obtenir_regles()                 # Liste toutes les règles
    def ajouter_regle(...)               # Ajoute une règle
    def nombre_regles()                  # Compte les règles
```

### 3. `moteur_inference.py` - Moteur d'Inférence

```python
class MoteurInference:
    """Implémente le chaînage avant."""
    
    # Attributs
    base_faits: BaseFaits
    base_regles: BaseRegles
    seuil_confiance: float = 0.4
    
    # Méthodes principales
    def evaluer_regle(regle)             # Évalue une règle
    def inferer()                        # Lance l'inférence
    def afficher_resultats(estimations)  # Affiche les résultats
    
    # Méthodes auxiliaires
    def verifier_condition(cle, valeurs)
    def verifier_conditions_excluantes(regle)
    def calculer_ratio_conditions_requises(regle)
    def calculer_bonus_optionnels(regle)
```

### 4. `main.py` - Point d'Entrée Console

```python
class SystemeExpertPrixPC:
    """Orchestre le système expert."""
    
    def executer()      # Lance le cycle complet
    def afficher_regles()
    def reinitialiser()

def main():             # Menu principal
```

### 5. `gui.py` - Interface Graphique

```python
class SystemeExpertGUI:
    """Interface Tkinter thème Hacker."""
    
    def _creer_banniere()
    def _creer_section_specifications()
    def _creer_boutons()
    def _creer_zone_resultats()
    def _lancer_estimation()
    def executer()
```

---

## 🚀 Installation

### Prérequis

- **Python 3.8+** installé
- **Tkinter** (inclus avec Python sur Windows/Mac)

### Vérification de l'Installation

```bash
# Vérifier Python
python --version

# Vérifier Tkinter
python -c "import tkinter; print('Tkinter OK')"
```

### Téléchargement

```bash
# Cloner ou télécharger le projet
cd systeme_expert_pc/
```

---

## 💻 Utilisation

### Mode Console

```bash
python main.py
```

**Exemple de session :**
```
=================================================================
    SYSTEME EXPERT - ESTIMATION PRIX PC PORTABLE
=================================================================

    MENU PRINCIPAL
----------------------------------------
  1. Lancer une estimation de prix
  2. Afficher les règles du système
  3. Quitter
----------------------------------------
Votre choix (1-3) : 1

Quelle est la taille de l'écran ?
  1. 14 pouces
  2. 15.6 pouces
  3. 16 pouces
  4. 17 pouces ou plus
Votre choix (numero) : 2
...
```

### Mode Interface Graphique

```bash
python gui.py
```

L'interface graphique propose :
- Menus déroulants pour les spécifications
- Cases à cocher pour les options
- Boutons d'action stylisés
- Terminal de résultats avec affichage futuriste

---

## 📖 Description des Modules

### Module `BaseFaits`

#### Spécifications Collectées (11 critères)

| Critère | Type | Exemple |
|---------|------|---------|
| Taille écran | Choix multiple | "15.6 pouces" |
| Usage | Choix multiple | "Gaming" |
| Processeur | Choix multiple | "Intel Core i7" |
| Génération CPU | Choix multiple | "Dernière génération (2024-2025)" |
| RAM | Choix multiple | "16 Go" |
| Stockage | Choix multiple | "SSD 1 To" |
| Carte graphique | Choix multiple | "NVIDIA RTX 4060" |
| Écran | Choix multiple | "Full HD (1920x1080)" |
| Taux rafraîchissement | Choix multiple | "144 Hz" |
| Marque | Choix multiple | "ASUS" |
| Poids | Choix multiple | "Léger (1.3-2 kg)" |

#### Options Booléennes (6 options)

| Option | Type | Description |
|--------|------|-------------|
| Pavé numérique | Oui/Non | Présence d'un pavé numérique |
| Clavier rétroéclairé | Oui/Non | Éclairage du clavier |
| Clavier RGB | Oui/Non | Éclairage RGB personnalisable |
| Thunderbolt | Oui/Non | Port Thunderbolt |
| Webcam HD | Oui/Non | Webcam HD ou supérieure |
| Lecteur empreinte | Oui/Non | Capteur d'empreintes digitales |

### Module `BaseRegles`

#### Anatomie d'une Règle

```python
{
    "nom": "Milieu/haut de gamme",
    "prix_min": 1200,
    "prix_max": 1799,
    "description": "PC performant pour gaming et création",
    
    # Conditions OBLIGATOIRES (au moins 50% doivent être vraies)
    "conditions_requises": {
        "processeur": ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7"],
        "ram": ["16 Go", "32 Go"]
    },
    
    # Conditions OPTIONNELLES (ajoutent un bonus de confiance)
    "conditions_optionnelles": {
        "carte_graphique": ["NVIDIA RTX 3060", "NVIDIA RTX 4060"],
        "taux_rafraichissement": ["120 Hz", "144 Hz"],
        "clavier_retroeclaire": True
    },
    
    # Conditions EXCLUANTES (si vraie → règle rejetée)
    "conditions_excluantes": {
        "processeur": ["Intel Celeron / Pentium"],
        "ram": ["4 Go", "8 Go"]
    },
    
    "confiance_base": 0.82
}
```

### Module `MoteurInference`

#### Algorithme d'Évaluation d'une Règle

```
ENTRÉE: règle, faits_utilisateur

1. VÉRIFIER CONDITIONS EXCLUANTES
   SI une condition excluante est satisfaite:
       RETOURNER (False, 0.0)

2. CALCULER RATIO CONDITIONS REQUISES
   ratio = nb_requises_satisfaites / nb_requises_totales
   SI ratio < 0.5:
       RETOURNER (False, 0.0)

3. CALCULER SCORE DE CONFIANCE
   confiance = confiance_base × (0.7 + 0.3 × ratio)

4. AJOUTER BONUS OPTIONNELS
   bonus = (nb_optionnelles_satisfaites / nb_optionnelles_totales) × 0.15
   confiance = min(1.0, confiance + bonus)

5. RETOURNER (True, confiance)
```

---

## 📊 Base de Règles

### Gammes de Prix

| # | Gamme | Prix | Description |
|---|-------|------|-------------|
| 1 | Entrée de gamme | < 500€ | PC basique pour usage léger |
| 2 | Petit budget | 500-799€ | PC polyvalent quotidien |
| 3 | Bon rapport qualité/prix | 800-1199€ | PC performant standard |
| 4 | Milieu/haut de gamme | 1200-1799€ | Gaming et création |
| 5 | Haut de gamme / Créateur | 1800-2499€ | Professionnels |
| 6 | Premium / Workstation | > 2500€ | Ultra haut de gamme |

### Règles Spécifiques

| # | Nom | Spécificité |
|---|-----|-------------|
| 7 | Gaming milieu de gamme | Usage = Gaming + GPU dédié |
| 8 | MacBook Air/Pro | Marque = Apple + Puce M1/M2 |

---

## ⚙️ Algorithme d'Inférence

### Processus Complet du Chaînage Avant

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 1: COLLECTE                            │
│                                                                 │
│   Utilisateur ──► Questionnaire ──► Base de Faits              │
│                                                                 │
│   Exemple:                                                      │
│   faits = {                                                     │
│       "processeur": "Intel Core i7",                           │
│       "ram": "16 Go",                                          │
│       "carte_graphique": "NVIDIA RTX 4060",                    │
│       ...                                                      │
│   }                                                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 2: INFÉRENCE                           │
│                                                                 │
│   POUR chaque règle dans base_regles:                          │
│       │                                                        │
│       ├──► Vérifier conditions excluantes                      │
│       │    SI excluante satisfaite → IGNORER règle             │
│       │                                                        │
│       ├──► Calculer ratio conditions requises                  │
│       │    SI ratio < 50% → IGNORER règle                      │
│       │                                                        │
│       ├──► Calculer score de confiance                         │
│       │    score = base × (0.7 + 0.3 × ratio) + bonus          │
│       │                                                        │
│       └──► SI score > seuil (40%)                              │
│            AJOUTER aux estimations                              │
│                                                                 │
│   FIN POUR                                                      │
│                                                                 │
│   TRIER estimations par score décroissant                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 3: RÉSULTATS                           │
│                                                                 │
│   Estimations triées:                                          │
│   1. Milieu/haut de gamme (1200-1799€) - 85%                  │
│   2. Bon rapport qualité/prix (800-1199€) - 65%               │
│   3. Gaming milieu de gamme (1200-1799€) - 60%                │
└─────────────────────────────────────────────────────────────────┘
```

### Formule de Calcul du Score

$$
\text{Score} = \min\left(1.0, \text{confiance\_base} \times (0.7 + 0.3 \times R) + B\right)
$$

Où :
- $R$ = ratio des conditions requises satisfaites
- $B$ = bonus des conditions optionnelles ($\leq 0.15$)

---

## 🎨 Interface Graphique

### Thème Hacker/Cyberpunk

| Élément | Couleur | Code Hex |
|---------|---------|----------|
| Fond principal | Noir profond | `#0a0a0a` |
| Fond panneaux | Gris sombre | `#0d1117` |
| Texte principal | Vert néon | `#00ff00` |
| Accent secondaire | Cyan | `#00ffff` |
| Avertissement | Jaune | `#ffff00` |
| Alerte | Orange | `#ff6600` |

### Éléments de l'Interface

1. **Bannière ASCII** - Logo stylisé du système
2. **Section Spécifications** - 11 menus déroulants en 2 colonnes
3. **Section Options** - 6 cases à cocher
4. **Boutons d'Action** :
   - `[ EXECUTE ANALYSIS ]` - Lance l'estimation
   - `[ RESET SYSTEM ]` - Réinitialise
   - `[ VIEW RULES ]` - Affiche les règles
   - `[ HELP ]` - Aide
5. **Terminal de Sortie** - Affichage stylisé des résultats

### Indicateurs de Confiance

```
HIGH   (80-100%) : ████████████████████ [Vert]
MEDIUM (60-80%)  : ████████████░░░░░░░░ [Jaune]
LOW    (<60%)    : ████████░░░░░░░░░░░░ [Orange]
```

---

## 📝 Exemples

### Exemple 1 : PC Gaming Milieu de Gamme

**Entrées :**
```
Processeur: Intel Core i7
RAM: 16 Go
Carte graphique: NVIDIA RTX milieu de gamme (RTX 3060, 4060)
Usage: Gaming
Taux rafraîchissement: 144 Hz
```

**Résultat :**
```
┌──────────────────────────────────────────────────────────────┐
│  RESULT #1: MILIEU/HAUT DE GAMME
├──────────────────────────────────────────────────────────────┤
│  [PRICE RANGE]  1200 - 1799 EUR
│  [CONFIDENCE]   85.2% [HIGH]
│  [INDICATOR]    ████████████████████
│  [INFO]         PC performant pour gaming et création
└──────────────────────────────────────────────────────────────┘
```

### Exemple 2 : MacBook Air

**Entrées :**
```
Marque: Apple
Processeur: Apple M2
RAM: 8 Go
Stockage: SSD 256 Go
```

**Résultat :**
```
┌──────────────────────────────────────────────────────────────┐
│  RESULT #1: BON RAPPORT QUALITE/PRIX
├──────────────────────────────────────────────────────────────┤
│  [PRICE RANGE]  800 - 1199 EUR
│  [CONFIDENCE]   88.0% [HIGH]
│  [INDICATOR]    ████████████████████
│  [INFO]         MacBook Air configuration de base
└──────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Avertissement

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════╗
║                    ⚠️  AVERTISSEMENT IMPORTANT  ⚠️                  ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Ce système expert est UNIQUEMENT à but ÉDUCATIF et PÉDAGOGIQUE. ║
║                                                                   ║
║  Les estimations de prix sont INDICATIVES et peuvent varier       ║
║  selon :                                                          ║
║                                                                   ║
║    • Les promotions et offres en cours                           ║
║    • La disponibilité des produits                               ║
║    • Le marché et la région d'achat                              ║
║    • Les configurations exactes des modèles                      ║
║                                                                   ║
║  Consultez les sites marchands pour des prix réels.              ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📄 Licence

Ce projet est développé dans le cadre d'un **TP universitaire** en Intelligence Artificielle.

**Usage** : Éducatif uniquement

---

<div align="center">

**Développé avec 💻 par l'équipe TP IA - Novembre 2025**

```
[SYS_EXPERT v2.0] :: Forward Chaining Inference Engine
```

</div>
