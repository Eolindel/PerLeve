# PerLeve
Script pour générer des permutations de binômes pour une liste d'élèves.

Il y a deux scripts :
- semaines.py pour créer une liste de semaines pour lesquelles il y a besoin de permutation ce script permet génère un fichier csv éditable à la main pour sélectionner les semaines ou dates nécessitant de générer une liste de binômes
- permutation.py qui prend en entrée deux fichiers csv : un pour les semaines, l'autre pour les élèves.

En sortie, un fichier csv est automatiquement généré, il est également aussi possible d'avoir un fichier LaTeX compilable pour avoir un  pdf un peu plus esthétique

Il est également possible de faire un tirage aléatoire pour les tables afin de placer les binômes aléatoirement dans la pièce, par défaut, les paillasses paire et impaires sont séparées. Sinon, chaque binôme se voir attribuer un numéro sans distinction des groupes pairs et impairs.

Deux fichiers d'exemples sont fournis pour lancer le programme, le fichier d'élèves correspond à une extraction automatique faite par proNote.

Remarque : il ne peut pas y avoir de permutation pour plus de semaines que le nombre d'élèves du groupe -1, s'il y a plus de semaines que demandé, alors un nouveau jeu de permutation commence. L'algorithme de création de binômes est celui de Round Robin.

Le fichier d'exemple utilise des noms et élèves fictifs.

Ce script est mis à disposition sous licence AGPLv3
