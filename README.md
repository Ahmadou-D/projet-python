# 🎮 Python Strategy Mini-Games : Snort & Dodgem

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Console](https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge) ![Algorithm](https://img.shields.io/badge/Logic-2D%20Arrays-blue?style=for-the-badge)

## 📝 Présentation du projet
Ce dépôt regroupe deux mini-jeux de plateau et de stratégie développés intégralement en **Python**. Conçus pour être joués à deux dans le terminal, ils mettent en pratique des concepts algorithmiques fondamentaux tels que la manipulation de listes à deux dimensions, la validation logique des coups et l'architecture de boucles de jeu.

## 🎲 Jeu 1 : Snort
**Snort** est un jeu de placement territorial où deux joueurs s'affrontent sur un plateau carré initialement vide.

* **Objectif** : Placer ses pions de manière à saturer l'espace. Le premier joueur qui ne peut plus jouer a perdu.
* **Règles** : 
  * Joueur 1 (Pions `x`) / Joueur 2 (Pions `o`).
  * Les cases vides sont représentées par un point (`.`).
  * **Contrainte stricte** : Un pion ne peut *jamais* être posé sur une case adjacente (orthogonalement) à un pion adverse.
* **Implémentation technique** : Gestion matricielle du plateau, vérification algorithmique des coups valides en temps réel, affichage numéroté clair en console.

## 🏎️ Jeu 2 : Dodgem
**Dodgem** est un jeu de déplacement abstrait et de blocage.

* **Objectif** : Faire sortir tous ses pions du plateau avant l'adversaire, ou le bloquer de sorte qu'il n'ait plus de coup légal.
* **Règles** :
  * Joueur 1 (`x`) : Déplace ses pions vers le Haut, la Gauche ou la Droite.
  * Joueur 2 (`o`) : Déplace ses pions vers le Bas, le Haut ou la Droite.
  * Un pion réussit à sortir du plateau s'il atteint le bord correspondant à sa direction de sortie.
* **Implémentation technique** : Détection des déplacements aux frontières de la grille (out of bounds), calcul dynamique des conditions de victoire et de blocage, système de saisie sécurisé.

## 📂 Structure du dépôt
* `snort.py` : Code source exécutable du jeu Snort.
* `snort_documentation.txt` : Documentation technique et règles détaillées.
* `Dodgem.py` : Code source exécutable du jeu Dodgem.
* `Dodgem_documentation.txt` : Documentation technique et règles détaillées.

## 🚀 Comment jouer ?
Assurez-vous de disposer de Python 3 sur votre machine. Clonez le dépôt et lancez simplement le fichier de votre choix depuis votre terminal :

```bash
python snort.py
# ou
python Dodgem.py
