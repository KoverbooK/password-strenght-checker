# password-strenght-checker
**A Python tool to assess the strenght of a password depending on several security criterias.**


## Table des matières
1. [Description](#description)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Tests](#tests)

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
   git clone https://github.com/Koverbook/password-strength-checker.git
   cd password-strenght-checker
   ```

## Utilisation
### Mode 1 : Test rapide via arguments

Vous pouvez tester un mot de passe en le passant directement comme argument dans la ligne de commande :
```bash
python strenghtCheck.py --mdp MonMotDePasse123!
```

### Mode 2 : Saisie sécurisée du mot de passe

Si vous souhaitez que le mot de passe soit saisi de manière sécurisée (masqué), vous pouvez utiliser le mode sécurisé :
```bash
python strenghtCheck.py --secure-mode
```
Saisir le mot de passe.
Une fois le mot de passe saisi, l'outil affichera la force du mot de passe sur une échelle de 0 à 8.

### Mode 3 : Tests par défaut

Si vous ne spécifiez aucun mot de passe, le programme effectuera des tests sur un ensemble de mots de passe pré-définis pour vérifier leur sécurité.
```bash
python strenghtCheck.py
```

## Test

Tu peux tester plusieurs mots de passe en utilisant les modes décrits ci-dessus, ou en créant un fichier test.py contenant une suite de mots de passe que tu veux analyser (futur).
