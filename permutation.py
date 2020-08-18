#!/usr/bin/env python3
import math
import csv
import random
import locale
import datetime
from operator import itemgetter, attrgetter
import os
listEleves = []
listSemaine = []


""" Paramètres pour le programme  """
fichierEleve = 'eleves.csv'
fichierSemaines = 'semaines2020.csv'
fichierSortie = 'TaleS2'
#Afficher un numéro de table tiré aléatoirement pour chaque binôme
assignerTable = True
#Générer un fichier Tex pour une sortie plus visuelle, un fichier csv est automatiquement généré
sortieLatex = True

"""
PROGRAMME
"""
locale.setlocale(locale.LC_ALL, '')


"""
Lecture du fichier d'entrée nommé eleves.csv séparé par des ';" et pas des virgules (export pronote), une première ligne est ignorée, 
ensuite, on suppose qu'il y a un élève par ligne et que le premier élement de chaque ligne est le nom complet de l'élève
"""
with open( fichierEleve,  newline='') as f:
    reader = csv.reader(f,delimiter=";")
    next(reader)
    for row in reader:
        listEleves.append(row[0])		
        print(row[0])
"""
lecture du fichier des semaines pour savoir pour combien de semaines il y a besoin de permutations
si le nombre de semaines est supérieur au nombre de permutations possibles, alors un nouveau jeu de permutations est crée de manière à remplir le calendrier
le format d'entrée est une ligne initiale de commentaire, puis 'flag', 'jour', 'commentaire'
si flag contient quelque chose alors la semaine n'est pas utilisée dans l'emploi du temps. 
Le jour est la date du TP pour la semaine correspondante 
 Le commentaire est juste pour s'aider
"""

with open(fichierSemaines,  newline='') as f:
	reader = csv.reader(f,delimiter=",")
	next(reader)
	for row in reader:
		if row[0] == '':
			listSemaine.append(row[1])		
			#print(row[1])

print("Génération des permutation pour {} semaines.".format( len(listSemaine) ) )
print(listSemaine)

def create_schedule(list):
    """ Creer une liste de permutations pour faire des binômes   """ 
    s = []
    """ Gestion des listes impaires """
    if len(list) % 2 == 1: list = list + [""]
    for i in range(len(list)-1):
        mid = int(len(list) / 2)
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()	
        s = s + [ zip(l1, l2) ]
        list.insert(1, list.pop())
    return s


listePaires = create_schedule(listEleves)


output = open(fichierSortie + '.csv','w')


if sortieLatex == True:
	outputLatex = open(fichierSortie +'.tex','w')
	outputLatex.write(r"""\documentclass[twoside,a4paper,12pt]{article}
\title{Liste Binômes}
\date{}
\usepackage[french]{babel}
\usepackage{amsmath}
\usepackage{array}
\usepackage[utf8]{inputenc}
\usepackage[top=20mm,bottom=20mm,left=20mm, right=20mm]{geometry}
\usepackage{pdfpages}
\usepackage[justification=centering]{caption}
\usepackage{verbatim}
\usepackage{multicol}
\usepackage{float}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{subfigure}
\usepackage{verbatim} 
\usepackage{mathrsfs}
\usepackage{textcomp}
\usepackage{cancel}
\usepackage{amssymb}
\usepackage{tabularx}
\usepackage{hyperref}
\hypersetup{
	pdfauthor={},
	pdfkeywords={},
    colorlinks,%
    citecolor=blue,%
    filecolor=blue,%
    linkcolor=blue,%
    urlcolor=blue
}
\usepackage{hypcap}
\usepackage{booktabs}
\author{}
\date{}
\usepackage{mathpazo}
\usepackage{colortbl}
\definecolor{title}{HTML}{e7d9eb}
\definecolor{pair}{HTML}{e3f4e0}
\definecolor{impair}{HTML}{fee7c7}
\renewcommand{\arraystretch}{1.2}
\begin{document}""")

for i in listSemaine:
	textPair=''
	textImpair=''
	if sortieLatex == True:
		textPairLatex=''
		textImpairLatex=''
	#S'il n'y plus de permutation de binôme, on en régénère une après avoir mélangé la liste initiale d'élèves
	if len(listePaires) == 0:
		random.shuffle(listEleves)
		listePaires = create_schedule(listEleves)
	#On récupère une liste de binôme de la liste générée
	listeBinome = list(listePaires.pop())
	tableListe = list(range(1, len(list(listeBinome))+1 ) ) 
	if assignerTable == True:
		random.shuffle(tableListe)
	tableBinome = list(zip( tableListe, listeBinome) )
	tableBinome.sort(key=itemgetter(0))
	#On récupère le jour de la semaine correspondant à la date
	jour = datetime.datetime.strptime(i,"%d-%m-%Y" )
	output.write(','+jour.strftime("%A").capitalize()+','+str(i)+"\n")
	if sortieLatex ==  True:
		outputLatex.write(r'\begin{tabular}{|c|l|l|}'+"\n"+r'\hline\multicolumn{3}{|c|}{\cellcolor{title} \raisebox{-2pt}{\textbf{\Large '+jour.strftime("%A").capitalize()+' '+str(i)+r"}}}\\\hline"+"\n")
	for triplette in tableBinome:
		if assignerTable == True:
			if triplette[0] % 2 == 1:
				textImpair += str(triplette[0])+','+triplette[1][0]+','+triplette[1][1]+"\n"
				if sortieLatex ==  True:
					textImpairLatex += '\cellcolor{impair}' + str(triplette[0])+' & \cellcolor{impair}'+triplette[1][0]+' & \cellcolor{impair}'+triplette[1][1]+r'\\ \hline'+"\n"
			else:
				textPair += str(triplette[0])+','+triplette[1][0]+','+triplette[1][1]+"\n"
				if sortieLatex ==  True:
					textPairLatex += '\cellcolor{pair}' + str(triplette[0])+' & \cellcolor{pair}'+triplette[1][0]+' & \cellcolor{pair}'+triplette[1][1]+r'\\ \hline'+"\n"
	output.write(textImpair)
	output.write(textPair)
	output.write("\n\n")
	if sortieLatex == True:
		outputLatex.write(textImpairLatex)
		outputLatex.write(textPairLatex)
		outputLatex.write(r'\end{tabular}'+"\n\n")
	#for paire in listeBinome:

if sortieLatex == True:
	outputLatex.write(r'\end{document}')
	outputLatex.close()
	os.system('pdflatex '+ fichierSortie  + '.tex > compilation-latex.log')


output.close()

