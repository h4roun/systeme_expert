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

</div>

---

## 📋 À Propos

Ce dépôt contient **deux implémentations** d'un système expert pour estimer la gamme de prix d'un ordinateur portable basé sur ses spécifications techniques.

Les deux versions utilisent le **chaînage avant** (forward chaining) et offrent une interface graphique avec un thème Hacker/Cyberpunk.

---

## 🔀 Versions Disponibles

| Branche | Description | Technologies |
|---------|-------------|--------------|
| [`main`](../../tree/main) | **Implémentation Manuelle** - Moteur d'inférence développé from scratch | Python, Tkinter |
| [`experta`](../../tree/experta) | **Implémentation Experta** - Utilise la bibliothèque professionnelle Experta | Python, Experta, Tkinter |

### 🛠️ Version Manuelle (`main`)

Implémentation pédagogique d'un moteur d'inférence en chaînage avant sans dépendances externes.

**Points forts :**
- ✅ Compréhension approfondie des mécanismes internes
- ✅ Code commenté et documenté
- ✅ Aucune dépendance externe (sauf Tkinter)
- ✅ Architecture modulaire claire

```bash
# Basculer vers cette version
git checkout main
```

### 🔧 Version Experta (`experta`)

Implémentation utilisant la bibliothèque **Experta**, inspirée de CLIPS, avec l'algorithme RETE.

**Points forts :**
- ✅ Utilisation de l'algorithme RETE (pattern matching efficace)
- ✅ Syntaxe déclarative avec décorateurs `@Rule`
- ✅ Gestion de priorité avec `salience`
- ✅ Standard professionnel

```bash
# Basculer vers cette version
git checkout experta

# Installer la dépendance
pip install experta
```

---

## 🚀 Installation Rapide

### Prérequis
- Python 3.8+
- Tkinter (inclus avec Python)

### Cloner le dépôt

```bash
git clone https://github.com/h4roun/systeme_expert.git
cd systeme_expert
```

### Lancer le projet

```bash
# Mode console
python main.py

# Mode interface graphique
python gui.py
```

---

## 📊 Comparaison des Implémentations

| Aspect | Version Manuelle | Version Experta |
|--------|------------------|-----------------|
| **Pattern Matching** | Boucles manuelles | Algorithme RETE |
| **Syntaxe des règles** | Dictionnaires Python | Décorateurs `@Rule` |
| **Priorité des règles** | Gestion manuelle | `salience` intégrée |
| **Dépendances** | Aucune | `experta` |
| **Complexité** | Plus de code | Plus concis |
| **Objectif pédagogique** | Comprendre le fonctionnement | Utiliser un outil professionnel |

---

## 🎯 Fonctionnalités

- ✅ Questionnaire interactif (console et GUI)
- ✅ 8 règles d'estimation de prix
- ✅ 6 gammes de prix (< 500€ à > 2500€)
- ✅ Score de confiance calculé
- ✅ Interface graphique thème "Hacker"
- ✅ Architecture modulaire

---

## 📖 Documentation Détaillée

Chaque branche contient son propre fichier `README.md` avec :
- Architecture détaillée
- Explication des concepts théoriques
- Documentation du code
- Exemples d'utilisation

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
║  selon le marché, les promotions, et la région d'achat.          ║
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

**Développé avec 💻 - Novembre 2025**

```
[SYS_EXPERT v2.0] :: Forward Chaining Inference Engine
```

</div>
