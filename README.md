# 🖥️ Système Expert - Estimation de Prix de PC Portable (EXPERTA)

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
║  ███████╗██╗  ██╗██████╗ ███████╗██████╗ ████████╗ █████╗                             ║
║  ██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗                            ║
║  █████╗   ╚███╔╝ ██████╔╝█████╗  ██████╔╝   ██║   ███████║                            ║
║  ██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ██╔══██║                            ║
║  ███████╗██╔╝ ██╗██║     ███████╗██║  ██║   ██║   ██║  ██║                            ║
║  ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                            ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
```

**Système Expert d'Estimation de Prix de PC Portable**

*Version utilisant la bibliothèque EXPERTA*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Experta](https://img.shields.io/badge/Experta-1.9.4-orange.svg)](https://pypi.org/project/experta/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](#)

> 📌 **Cette branche contient l'implémentation utilisant Experta.** Pour la version manuelle (sans bibliothèque externe), voir la branche [`main`](../../tree/main).

</div>

---

## 📋 Table des Matières

1. [Introduction](#-introduction)
2. [Qu'est-ce qu'Experta ?](#-quest-ce-quexperta-)
3. [Architecture du Projet](#-architecture-du-projet)
4. [Installation](#-installation)
5. [Utilisation](#-utilisation)
6. [Structure des Fichiers](#-structure-des-fichiers)
7. [Concepts Clés d'Experta](#-concepts-clés-dexperta)
8. [Base de Règles](#-base-de-règles)
9. [Algorithme RETE](#-algorithme-rete)
10. [Interface Graphique](#-interface-graphique)
11. [Exemples de Code](#-exemples-de-code)
12. [Comparaison avec l'implémentation manuelle](#-comparaison-avec-limplémentation-manuelle)
13. [Avertissement](#-avertissement)

---

## 🎯 Introduction

Ce projet implémente un **système expert** utilisant la bibliothèque **Experta** pour estimer la gamme de prix d'un ordinateur portable en fonction de ses spécifications techniques.

### Objectifs Pédagogiques

- Utiliser une bibliothèque professionnelle de systèmes experts
- Comprendre l'algorithme RETE pour le pattern matching
- Définir des faits (Facts) et des règles (@Rule) avec Experta
- Comparer avec une implémentation manuelle

### Fonctionnalités

- ✅ Utilisation de la bibliothèque Experta
- ✅ Algorithme RETE pour l'inférence
- ✅ Définition de Facts personnalisés
- ✅ Règles avec décorateur @Rule
- ✅ Salience pour priorité des règles
- ✅ Interface graphique thème "Hacker"
- ✅ Mode test intégré

---

## 🔧 Qu'est-ce qu'Experta ?

**Experta** est une bibliothèque Python pour construire des systèmes experts, fortement inspirée de **CLIPS** (C Language Integrated Production System).

### Caractéristiques Principales

| Caractéristique | Description |
|-----------------|-------------|
| **Algorithme RETE** | Pattern matching efficace pour les règles |
| **Facts** | Objets représentant les connaissances |
| **Rules** | Règles SI...ALORS avec décorateurs Python |
| **KnowledgeEngine** | Moteur d'inférence centralisé |
| **Salience** | Priorité des règles |
| **DefFacts** | Faits initiaux automatiques |

### Installation

```bash
pip install experta
```

### Exemple Simple (Traffic Light)

```python
from experta import *

class Light(Fact):
    """Info about the traffic light."""
    pass

class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

# Utilisation
engine = RobotCrossStreet()
engine.reset()
engine.declare(Light(color='green'))
engine.run()  # Affiche: Walk
```

---

## 🏗️ Architecture du Projet

```
systeme_expert/
│
├── 📄 __init__.py          # Package Python
├── 📄 faits.py             # Classes Fact (SpecificationPC, Estimation)
├── 📄 regles.py            # KnowledgeEngine avec @Rule
├── 📄 main.py              # Point d'entrée console
├── 📄 gui.py               # Interface graphique Tkinter
├── 📄 requirements.txt     # Dépendances (experta)
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
│                     EXPERTA KNOWLEDGE ENGINE                         │
│                      (SystemeExpertPrixPC)                           │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │                      regles.py                                  ││
│  │                                                                 ││
│  │    ┌──────────────────┐         ┌──────────────────┐           ││
│  │    │   FACTS          │         │   RULES          │           ││
│  │    │ (faits.py)       │ ──────► │ (@Rule)          │           ││
│  │    │                  │  RETE   │                  │           ││
│  │    │ • SpecificationPC│  ALGO   │ • Exclusion rules│           ││
│  │    │ • Estimation     │         │ • Price rules    │           ││
│  │    │ • GammeExclue    │         │ • Salience       │           ││
│  │    └──────────────────┘         └──────────────────┘           ││
│  │                                                                 ││
│  │                    ┌────────────────────────┐                   ││
│  │                    │   ALGORITHME RETE      │                   ││
│  │                    │   Pattern Matching     │                   ││
│  │                    └────────────────────────┘                   ││
│  │                                 │                               ││
│  │                                 ▼                               ││
│  │                    ┌────────────────────────┐                   ││
│  │                    │   ESTIMATIONS          │                   ││
│  │                    │   Triées par confiance │                   ││
│  │                    └────────────────────────┘                   ││
│  └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Prérequis

- **Python 3.8+** installé
- **pip** pour l'installation des packages

### Étapes d'Installation

```bash
# 1. Installer Experta
pip install experta

# 2. Vérifier l'installation
python -c "from experta import *; print('Experta OK')"

# 3. Naviguer vers le projet
cd systeme_expert_pc_experta/
```

### Vérification

```bash
# Tester le module regles.py
python regles.py
```

---

## 💻 Utilisation

### Mode Console

```bash
python main.py
```

**Menu principal :**
```
    MENU PRINCIPAL
----------------------------------------
  1. Lancer une estimation de prix
  2. Tester avec des valeurs prédéfinies
  3. Quitter
----------------------------------------
```

### Mode Interface Graphique

```bash
python gui.py
```

### Mode Test Rapide

```python
from regles import SystemeExpertPrixPC
from faits import SpecificationPC

# Créer le moteur
engine = SystemeExpertPrixPC()
engine.reset()

# Déclarer les spécifications
engine.declare(SpecificationPC(
    processeur="Intel Core i7",
    ram="16 Go",
    carte_graphique="NVIDIA RTX milieu de gamme (RTX 3060, 4060)",
    usage="Gaming"
))

# Exécuter l'inférence
engine.run()

# Obtenir les résultats
for est in engine.obtenir_estimations():
    print(f"{est['gamme']}: {est['confiance']*100:.1f}%")
```

---

## 📁 Structure des Fichiers

### 1. `faits.py` - Classes Fact

Définit les structures de données Experta :

```python
from experta import Fact

class SpecificationPC(Fact):
    """Fait représentant les spécifications d'un PC portable."""
    pass

class Estimation(Fact):
    """Fait représentant une estimation de prix."""
    pass

class GammeExclue(Fact):
    """Fait indiquant qu'une gamme est exclue."""
    pass
```

### 2. `regles.py` - KnowledgeEngine

Contient le moteur d'inférence avec toutes les règles :

```python
from experta import *

class SystemeExpertPrixPC(KnowledgeEngine):
    
    @DefFacts()
    def faits_initiaux(self):
        yield Fact(systeme="actif")
    
    @Rule(
        SpecificationPC(
            processeur=P(lambda x: x in ["Intel Core i7", "Intel Core i9"]),
            ram=L("16 Go")
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
```

### 3. `main.py` - Interface Console

Point d'entrée avec questionnaire interactif.

### 4. `gui.py` - Interface Graphique

Interface Tkinter avec thème Hacker/Cyberpunk.

---

## 📚 Concepts Clés d'Experta

### 1. Fact (Fait)

Un **Fact** est un objet qui représente une connaissance :

```python
from experta import Fact

class Light(Fact):
    """Représente un feu de circulation."""
    pass

# Utilisation
light = Light(color="green", position="north")
```

### 2. Rule (Règle)

Une **Rule** définit une condition et une action :

```python
from experta import Rule, KnowledgeEngine

class MyEngine(KnowledgeEngine):
    @Rule(Light(color='green'))
    def action_green(self):
        print("Feu vert - Avancer")
```

### 3. Field Constraints (Contraintes de Champ)

| Contrainte | Description | Exemple |
|------------|-------------|---------|
| `L(value)` | Literal - valeur exacte | `L("green")` |
| `P(func)` | Predicate - fonction de test | `P(lambda x: x > 10)` |
| `W()` | Wildcard - n'importe quelle valeur | `W()` |
| `~` | NOT - négation | `~L("red")` |
| `\|` | OR - disjonction | `L("green") \| L("yellow")` |
| `&` | AND - conjonction | `P(lambda x: x > 0) & P(lambda x: x < 10)` |

### 4. Conditional Elements (Éléments Conditionnels)

| Élément | Description |
|---------|-------------|
| `AND()` | Toutes les conditions doivent être vraies |
| `OR()` | Au moins une condition doit être vraie |
| `NOT()` | La condition ne doit PAS être vraie |
| `TEST()` | Test d'une expression Python |
| `EXISTS()` | Au moins un fait correspond |
| `FORALL()` | Tous les faits correspondent |

### 5. Salience (Priorité)

La **salience** définit l'ordre d'exécution des règles :

```python
@Rule(Light(color='red'), salience=100)  # Haute priorité
def urgent_stop(self):
    print("STOP IMMÉDIAT!")

@Rule(Light(color='yellow'), salience=50)  # Priorité moyenne
def slow_down(self):
    print("Ralentir")
```

### 6. DefFacts (Faits Initiaux)

Déclare des faits automatiquement au `reset()` :

```python
@DefFacts()
def initial_facts(self):
    yield Fact(initialized=True)
    yield Light(color="red")
```

---

## 📊 Base de Règles

### Gammes de Prix

| # | Gamme | Prix | Salience |
|---|-------|------|----------|
| 1 | Entrée de gamme | < 500€ | 50 |
| 2 | Petit budget | 500-799€ | 50-55 |
| 3 | Bon rapport qualité/prix | 800-1199€ | 50-65 |
| 4 | Milieu/haut de gamme | 1200-1799€ | 50-75 |
| 5 | Haut de gamme / Créateur | 1800-2499€ | 50-75 |
| 6 | Premium / Workstation | > 2500€ | 50-80 |

### Règles d'Exclusion (Salience = 100)

Les règles d'exclusion s'exécutent en **premier** :

```python
@Rule(
    SpecificationPC(
        processeur=P(lambda x: x in ["Intel Core i9", "AMD Ryzen 9"])
    ),
    salience=100
)
def exclure_entree_gamme_cpu_puissant(self):
    self.declare(GammeExclue(gamme="Entree de gamme", raison="CPU trop puissant"))
```

### Pattern Matching avec P()

```python
@Rule(
    SpecificationPC(
        processeur=P(lambda x: x in [
            "Intel Core i7", "AMD Ryzen 7"
        ]),
        ram=P(lambda x: x in ["16 Go", "32 Go"]),
        usage=L("Gaming")
    ),
    NOT(GammeExclue(gamme="Milieu/haut de gamme"))
)
def regle_gaming(self):
    # Action
```

---

## ⚙️ Algorithme RETE

### Qu'est-ce que RETE ?

**RETE** (prononcé "REE-tee", signifie "réseau" en latin) est un algorithme de pattern matching utilisé dans les systèmes experts.

### Avantages

1. **Efficacité** : Ne réévalue pas toutes les règles à chaque changement
2. **Mémorisation** : Garde en mémoire les correspondances partielles
3. **Incrémental** : Traite uniquement les changements

### Structure du Réseau RETE

```
                    ┌─────────────────┐
                    │   ROOT NODE     │
                    │  (Entrée faits) │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │ ALPHA    │   │ ALPHA    │   │ ALPHA    │
        │ NODE 1   │   │ NODE 2   │   │ NODE 3   │
        │ (Test    │   │ (Test    │   │ (Test    │
        │  CPU)    │   │  RAM)    │   │  GPU)    │
        └────┬─────┘   └────┬─────┘   └────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                    ┌──────────────┐
                    │  BETA NODE   │
                    │  (Join)      │
                    └──────┬───────┘
                           ▼
                    ┌──────────────┐
                    │ TERMINAL     │
                    │ NODE         │
                    │ (Action)     │
                    └──────────────┘
```

### Cycle d'Exécution

```
1. RESET     → Initialise le moteur, déclare les DefFacts
2. DECLARE   → Ajoute des faits au moteur
3. RUN       → Exécute l'algorithme RETE :
   │
   ├── a. Pattern Matching (Alpha + Beta nodes)
   ├── b. Conflict Resolution (Salience)
   ├── c. Fire Rule (Exécute l'action)
   └── d. Répète jusqu'à épuisement des règles
```

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

### Boutons

- `[ EXECUTE ANALYSIS ]` - Lance l'inférence Experta
- `[ RESET SYSTEM ]` - Réinitialise
- `[ RUN TEST ]` - Test avec valeurs prédéfinies
- `[ HELP ]` - Aide

---

## 💡 Exemples de Code

### Exemple 1 : Définir un Fact Personnalisé

```python
from experta import Fact

class Voiture(Fact):
    """Représente une voiture avec ses caractéristiques."""
    pass

# Utilisation
ma_voiture = Voiture(
    marque="Tesla",
    modele="Model 3",
    annee=2024,
    electrique=True
)
```

### Exemple 2 : Règle avec Conditions Multiples

```python
from experta import *

class DiagnosticAuto(KnowledgeEngine):
    @Rule(
        Voiture(
            marque=W(),  # N'importe quelle marque
            annee=P(lambda x: x < 2020),  # Avant 2020
            electrique=L(False)  # Non électrique
        )
    )
    def voiture_ancienne_essence(self):
        print("Cette voiture pourrait nécessiter plus d'entretien")
```

### Exemple 3 : Utilisation de OR

```python
@Rule(
    OR(
        SpecificationPC(processeur=L("Intel Core i9")),
        SpecificationPC(processeur=L("AMD Ryzen 9"))
    )
)
def cpu_haut_gamme(self):
    print("CPU haut de gamme détecté!")
```

### Exemple 4 : Utilisation de NOT

```python
@Rule(
    SpecificationPC(ram=L("32 Go")),
    NOT(GammeExclue(gamme="Haut de gamme"))
)
def ram_suffisante_haut_gamme(self):
    # S'exécute seulement si la gamme n'est pas exclue
    pass
```

### Exemple 5 : Variable Binding avec AS

```python
@Rule(AS.spec << SpecificationPC(usage=W()))
def afficher_usage(self, spec):
    print(f"Usage détecté: {spec['usage']}")
```

---

## 🔄 Comparaison avec l'Implémentation Manuelle

### Implémentation Manuelle (Projet Précédent)

```python
# Vérification manuelle des conditions
def evaluer_regle(self, regle):
    for cle, valeurs in regle["conditions_requises"].items():
        if not self.verifier_condition(cle, valeurs):
            return False
    return True
```

### Implémentation Experta (Ce Projet)

```python
# Pattern matching automatique avec @Rule
@Rule(
    SpecificationPC(
        processeur=P(lambda x: x in ["Intel Core i7"]),
        ram=L("16 Go")
    )
)
def ma_regle(self):
    # Action automatiquement déclenchée
    pass
```

### Tableau Comparatif

| Aspect | Implémentation Manuelle | Experta |
|--------|------------------------|---------|
| Pattern Matching | Manuel (boucles) | Automatique (RETE) |
| Priorité | Manuelle | Salience |
| Syntaxe | Dictionnaires | Décorateurs Python |
| Performance | O(n×m) | O(n) avec RETE |
| Complexité | Plus de code | Plus concis |
| Debugging | Difficile | Watchers intégrés |
| Standardisation | Non | Inspiré de CLIPS |

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

## 📚 Ressources

- [Documentation Experta](https://experta.readthedocs.io/)
- [PyPI - Experta](https://pypi.org/project/experta/)
- [GitHub - Experta](https://github.com/nilp0inter/experta)
- [CLIPS Official](http://clipsrules.sourceforge.net/)
- [Algorithme RETE - Wikipedia](https://en.wikipedia.org/wiki/Rete_algorithm)

---

## 📄 Licence

Ce projet est développé dans le cadre d'un **TP universitaire** en Intelligence Artificielle.

**Usage** : Éducatif uniquement

---

<div align="center">

**Développé avec 💻 par l'équipe TP IA - Novembre 2025**

```
[SYS_EXPERT v2.0] :: EXPERTA Knowledge Engine :: RETE Algorithm
```

</div>
