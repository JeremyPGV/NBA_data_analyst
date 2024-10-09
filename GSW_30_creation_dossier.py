# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 07:09:58 2023

@author: jerem
"""

nom_dossier = 'Match_'+ str(numero_match)

# Spécifiez le chemin où vous souhaitez créer le dossier
chemin_dossier = os.path.join(os.getcwd(), nom_dossier)

# Vérifiez si le dossier existe déjà
if not os.path.exists(chemin_dossier):
    # Créez le dossier
    os.mkdir(chemin_dossier)
    print(f"Dossier '{nom_dossier}' cree avec succes.")
else:
    print(f"Dossier '{nom_dossier}' existe deja.")
    sys.exit()  # Arrêtez le programme ici si le dossier existe déjà