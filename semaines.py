#!/usr/bin/env python3

"""
Crée une liste de semaines pour le programme permutation.py
chaque semaine qui a un 'flag' égal à '$' sera ignorée dans la liste des semaines pour lesquelles il y a besoin d'une permutation
le champ 'commentaire' est ignoré mais peut servir à avoir quelque chose de plus facilement lisible
"""

import csv
import datetime

"""
INITIALISATION DES PARAMÈTRES
"""

""" Jour de la semaine, 0: dimanche, 1 : lundi, 2 : mardi, 3 : mercredi, 4 : jeudi, 5 : vendredi, 6 : samedi   """
jour = 1
semaineDebut = 36 
semaineFin = 27
anneeDebut = 2020

""" PROGRAMME  """
listeSemaine = [['flag', 'jour', 'commentaire']]
def weekLine(semaine,annee,jour):
	comment = ''
	flag = ''
	if i == 52 or i == 1:
		comment = 'Vacances de Noël'
		flag = '$'
	elif i == 44 or i == 43:
		comment = 'Vacances de Toussaint ?'
		flag = '$'
	elif i >= 6 and i<=9:
		comment = 'Vacances de février ?'
	elif i >= 15 and i<=18:
		comment = 'Vacances de Pâques ?'
	#dateJour = datetime.datetime.strptime(str(annee) + '-W' + str(semaine) + '-' + str(jour), "%Y-W%W-%w")
	#Date format ISO 
	dateJour = datetime.datetime.strptime(str(annee) + '-W' + str(semaine) + '-' + str(jour), "%G-W%V-%u")
	#return [flag, dateJour.strftime("%d-%m-%Y"), semaine, annee, comment]
	return [flag, dateJour.strftime("%d-%m-%Y"), comment]


for i in range(semaineDebut,53):
	listeSemaine.append(weekLine(i,anneeDebut,jour))
for i in range(1,semaineFin+1):
	listeSemaine.append(weekLine(i,anneeDebut+1,jour))
for i in listeSemaine:
	print(i)
with open('semaines'+repr(anneeDebut)+'.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(listeSemaine) 
