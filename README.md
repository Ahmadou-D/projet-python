Ce projet regroupe deux mini-jeux de stratégie développés en Python:


Jeu 1 : Snort
Objectif

Deux joueurs s’affrontent sur un plateau carré vide.
Chacun place ses pions à tour de rôle, en respectant une règle :
Un pion ne peut pas être posé à côté (orthogonalement) d’un pion adverse.

Règles

Joueur 1 → Pions “x”
Joueur 2 → Pions “o”
Une case vide = “.”
Le joueur qui ne peut plus jouer perd la partie.

Points techniques

Gestion du plateau avec une liste à deux dimensions
Vérification automatique de la validité des coups
Boucle de jeu alternant les tours des joueurs
Affichage console clair et numéroté

Jeu 2 : Dodgem
Objectif
Deux joueurs déplacent leurs pions sur un plateau carré.
Le but est de sortir ses pions du plateau avant l’adversaire ou de le bloquer.

Règles

Joueur 1 (“x”) déplace ses pions vers le haut, la gauche ou la droite
Joueur 2 (“o”) déplace ses pions vers le bas, le haut ou la droite
Un pion sort du plateau s’il atteint le bord dans sa direction de sortie
Le premier joueur sans coup possible perd la partie

Points techniques

Détection des déplacements valides selon les règles
Gestion des conditions de victoire et blocage
Système de saisie utilisateur simple et contrôlé
Boucle de jeu claire et fluide

Technologies
Langage : Python 
Affichage : Console (texte)

Concepts utilisés : Boucles, conditions, listes à deux dimensions, fonctions.
