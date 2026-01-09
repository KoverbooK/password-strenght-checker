# password-strenght-checker
**A Python tool to assess the strenght of a password depending on several security criterias.**


## Table des matières
1. [Description](#description)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Exemple](#exemple)
5. [Limitation](#limitation)

## Description

Ce projet consiste en un **vérificateur de la force des mots de passe**, conçu pour analyser la robustesse d'un mot de passe en fonction de plusieurs critères :
- **Analyse de la longueur** : Vérifie si le mot de passe dépasse une certaine longueur pour augmenter sa robustesse.
- **Diversité des caractères** : Évalue la diversité des caractères utilisés (minuscules, majuscules, chiffres, symboles).
- **Analyse de la corrélation** : Évalue la "prévisibilité" d'un mot de passe.
  
Il permet également de tester rapidement des mots de passe via une interface en ligne de commande (CLI).

## Fonctionnalités

- **Mode sécurisé** : Permet de saisir un mot de passe masqué en mode terminal (CLI).
- **Mode rapide** : Permet de tester un mot de passe directement via les arguments en ligne de commande.

## Installation

### Prérequis

- Python 3.x, git
- Pip (gestionnaire de paquets Python)
- Clonez le repository :
   ```bash
   cd Downloads
   git clone https://github.com/KoverbooK/password-strength-checker.git
   cd password-strenght-checker
   ```

## Exemple

* Test rapide
```bash
python strenghtCheck.py --mdp MonMotDePasse123!
```
Le mot de passe est passé directement en ligne de commande.

* Test sécurisé
```bash
python strenghtCheck.py --secure-mode
```
Le mot de passe est passé de manière masquée.

* Conseils d'amélioration
```bash
python strenghtCheck.py --advice
```

* Tests par défaut
```bash
python strenghtCheck.py
```
Note un ensemble de mot de passe prédéfinie.

## Limitation
Ne détecte pas les mots de passe inspirés des mots du dictionnaire.
