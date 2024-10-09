# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:54:20 2023

@author: jerem
"""

""" ______________________________ Bibliothèques _________________________________ """

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox,TextArea, HPacker, VPacker)
from datetime import datetime, timedelta 
from matplotlib.patches import ConnectionPatch
import numpy as np
import os
from PIL import Image
import sys
from email.message import EmailMessage
import ssl
import smtplib

""" __________________ Couleurs équipes ________________________________"""

couleur1 = ['#1D428A','#C4CED4', '#00471B', '#0E2240'] # [GSW, SAS, MIL, DEN]
couleur2 = ['#FFC72C', '#000000','#EEE1C6','#FEC524'] # [GSW, SAS, MIL, DEN]



""" ____________________ Modif si changement de joueur  _________________________________ """

joueur_analyse = "S.Curry" #mettre le surnom du joueur qui sera affiché

equipe_analyse = "Warriors"

debut_fichier = "GSW_30_"

annee = "2023-2024"

saison = "Reg. Season" #"Preseason" #"Reg. Season" #ou Playoffs

taille_image_joueur = (334, 475) #(x,y) en pixel

arrier_plan = 'black'

joueur_nbr_post = "GSW #30 - PG"

serie_victoire_adversaire = input ("Nombre de victoire de l'adversaire : ")

serie_defaite_adversaire = input ("Nombre de défaite de l'adversaire : ")

indice_couleur = 0 # [GSW, SAS, MIL, DEN]

""" ______________________________ Exécution _________________________________ """


""" Chargement des fichiers excel """

# Charge le fichier Excel
nom_fichier = debut_fichier + "stats.xlsx"
nom_fichier_equipe = equipe_analyse + "_stats.xlsx"


# Lit le fichier Excel en utilisant pandas
dataframe = pd.read_excel(nom_fichier)
dataframe_equipe = pd.read_excel(nom_fichier_equipe)

numero_match = len(dataframe_equipe) #on prend le nombre de match joué par l'equipe
print ("C'est le match #",numero_match)


""" Vérification de la présence du joueur """


valeur_a_verifier = dataframe_equipe.iloc[0,0] #1,0 prgm ok, defaut 0,0

if valeur_a_verifier in dataframe.iloc[:,0].values :
    
    exec(open(debut_fichier+"import_selection_valeurs.py").read())
    exec(open(debut_fichier+"background_top.py").read())
    exec(open(debut_fichier+"creation_dossier.py").read())
    exec(open(debut_fichier+"host_page.py").read())
    exec(open(debut_fichier+"stats_recap.py").read())
    exec(open(debut_fichier+"impact_radar.py").read())
    exec(open(debut_fichier+"efficiency.py").read())
    exec(open(debut_fichier+"mail.py").read())
    
else :
    print("LE JOUEUR N'A PAS JOUE")