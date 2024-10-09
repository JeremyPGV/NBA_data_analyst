# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:09:26 2023

@author: jerem
"""

exec(open(debut_fichier+"background_top.py").read())


""" ____________ Contenu liseré gauche ________________________ """

text_lisere_1 = TextArea("PROGRAM", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.16, 0.55), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("- Player Stats", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.17, 0.45), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.4), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Impact", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.145, 0.37), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.065, 0.385), frameon = False)
ax.add_artist(ab_text_lisere_1)


text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.32), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Efficiency", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.16, 0.29), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.065, 0.305), frameon = False)
ax.add_artist(ab_text_lisere_1)


""" ____________ Contenu liseré droit _____________________________________ """


file_0 =image.imread(domicile_img)
imagebox = OffsetImage(file_0, zoom = zoom_equipe_domicile*3)
ab_image = AnnotationBbox(imagebox, (0.50, 0.5), frameon = False)
ax.add_artist(ab_image)

file_0 =image.imread(adversaire_img)
imagebox = OffsetImage(file_0, zoom = zoom_adversaire*3)
ab_image = AnnotationBbox(imagebox, (0.80, 0.5), frameon = False)
ax.add_artist(ab_image)



text_lisere_1 = TextArea("VS", textprops=dict(color="k", size=30, ha='left',va='baseline',weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.65, 0.5), frameon = False)
ax.add_artist(ab_text_lisere_1)



text_lisere_1 = TextArea("GAME "+ str(numero_match), textprops=dict(color="k", size=50, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.65, 0.3), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("ANALYSIS", textprops=dict(color="k", size=50, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.65, 0.25), frameon = False)
ax.add_artist(ab_text_lisere_1)


"""_______________________ trait de séparation _____________________________ """

file_0 =image.imread('images/dark_trait_v.png')
imagebox = OffsetImage(file_0, zoom = 1)
ab_image = AnnotationBbox(imagebox, (0.3, 0.4), frameon = False)
ax.add_artist(ab_image)


# """_______________________ cheverons _____________________________ """

# file_0 =image.imread('images/chevron.png')
# imagebox = OffsetImage(file_0, zoom = 0.1)
# ab_image = AnnotationBbox(imagebox, (0.92, 0.03), frameon = False)
# ax.add_artist(ab_image)




"""______________________  Sauvegarde image ________________________________"""

output_path = 'Match_'+ str(numero_match) +'/'+ joueur_analyse +'_page_1.png'
plt.savefig(output_path, bbox_inches='tight', pad_inches=0, transparent=False)

"""__________  Check taille image _________________________________________ """

def get_image_resolution(image_path):
    try:
        image = Image.open(image_path)
        width, height = image.size
        return width, height
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return None

image_path = output_path
resolution = get_image_resolution(image_path)

if resolution:
    print(f"Résolution de l'image : {resolution[0]} x {resolution[1]} pixels")