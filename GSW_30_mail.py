# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:51:24 2023

@author: jerem
"""

email_envoi = "jvnbadataanalyst@gmail.com"
email_password = "stirrgtuatnxaqnc"
email_reception = "jv.data.analyst@gmail.com"
email_reception2 = "nba2023nba2023nba@gmail.com"

Objet = debut_fichier + 'Match_' + str(numero_match) + "_" + saison + "_" + annee
Corps = " Analyse contenue en PJ"


em = EmailMessage()

em['From'] = email_envoi
em['To'] = email_reception
em['Subject'] = Objet
em.set_content(Corps)

# Chemin vers le dossier contenant les fichiers à joindre
dossier = 'Match_' + str(numero_match)

# Listez les fichiers dans le dossier
fichiers = os.listdir(dossier)

contexte = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexte) as smtp:
    smtp.login(email_envoi, email_password)
    
    # Attachez chaque fichier du dossier à l'email
    for fichier in fichiers:
        chemin_fichier = os.path.join(dossier,fichier)
        
        # Assurez-vous que le chemin est bien un fichier (et non un sous-dossier)
        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'rb') as piece_jointe:
                em.add_attachment(piece_jointe.read(), maintype='application', 
                                  subtype='octet-stream', filename=fichier)
    smtp.sendmail(email_envoi, email_reception, em.as_string())
    

print (" LE MAIL EST ENVOYE A JEREMY ! ")


em = EmailMessage()

em['From'] = email_envoi
em['To'] = email_reception2
em['Subject'] = Objet
em.set_content(Corps)

# Chemin vers le dossier contenant les fichiers à joindre
dossier = 'Match_' + str(numero_match)

# Listez les fichiers dans le dossier
fichiers = os.listdir(dossier)

contexte = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexte) as smtp:
    smtp.login(email_envoi, email_password)
    
    # Attachez chaque fichier du dossier à l'email
    for fichier in fichiers:
        chemin_fichier = os.path.join(dossier,fichier)
        
        # Assurez-vous que le chemin est bien un fichier (et non un sous-dossier)
        if os.path.isfile(chemin_fichier):
            with open(chemin_fichier, 'rb') as piece_jointe:
                em.add_attachment(piece_jointe.read(), maintype='application', 
                                  subtype='octet-stream', filename=fichier)
    smtp.sendmail(email_envoi, email_reception2, em.as_string())
    

print (" LE MAIL EST ENVOYE A THEO ! ")