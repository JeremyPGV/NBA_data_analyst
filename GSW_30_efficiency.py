# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:35:46 2023

@author: jerem
"""

categories = ["Field Goal (FG)", "Free Throws (FT)", "3-Points (3P)"]
values1 = [joueur_FGA,joueur_FTA, joueur_3PA]
values2 = [joueur_FGM,joueur_FTM, joueur_3PM]



# Create stacked bar chart
fig, ax = plt.subplots()
ax.bar(categories, values1, label='Attemped', color=couleur1[indice_couleur]) #jaune
ax.bar(categories, values2, bottom=values1, label='Scored', color=couleur2[indice_couleur]) #bleu

# Set chart labels and legend
font = {'family': 'sans serif', #arial, sans-serif, candara
        'weight': 'heavy',
        'size': 15,
        }

#    Add annotation values
for i, v1, v2 in zip(range(len(categories)), values1, values2):
   # if v1 + v2 >= 6:
        ax.text(i, v1/2, str(v1), ha='center', va='center',color=couleur2[indice_couleur], fontdict=font)
        ax.text(i, v1+v2/2, str(v2), ha='center', va='center',color=couleur1[indice_couleur] ,fontdict=font)
    
ax.legend (loc = "upper right")


output_path = 'Match_' + str(numero_match) +'/'+ joueur_analyse + '_page_4.png'
plt.savefig(output_path, bbox_inches='tight', pad_inches=0, transparent=True)

exec(open(debut_fichier+"background_top.py").read())

legend_box_graph = TextArea(joueur_analyse + ' efficiency (G.' + str(numero_match) + ')', 
                  textprops=dict(color="k", size=45, ha='left',va='baseline', weight ='bold'))
ab_legend = AnnotationBbox(legend_box_graph, (0.5, 0.63), frameon = False)
ax.add_artist(ab_legend)



file=image.imread('Match_' + str(numero_match) +'/'+ joueur_analyse + '_page_4.png')
imagebox = OffsetImage(file, zoom = 1.45)
ab_file = AnnotationBbox(imagebox, (0.64, 0.33), frameon = False)
ax.add_artist(ab_file)

"""_______________________ Trait vertical _____________________________ """

file_0 =image.imread('images/dark_trait_v.png')
imagebox = OffsetImage(file_0, zoom = 1)
ab_image = AnnotationBbox(imagebox, (0.3, 0.35), frameon = False)
ax.add_artist(ab_image)



""" ____________ Pourcentage efficacité ________________________ """

text_lisere_1 = TextArea(str(round(joueur_E2PTS*100,)) + '%', textprops=dict(color="k", size=20, ha='left',va='baseline', weight = 'bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.45, 0.56), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Team : " + str(round(equipe_E2PTS*100,)) + '%', textprops=dict(color="k", size=20, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.45, 0.54), frameon = False)
ax.add_artist(ab_text_lisere_1)


text_lisere_1 = TextArea(str(round(joueur_EFT*100,)) + '%', textprops=dict(color="k", size=20, ha='left',va='baseline', weight = 'bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.66, 0.56), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Team : " + str(round(equipe_EFT*100,)) + '%', textprops=dict(color="k", size=20, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.66, 0.54), frameon = False)
ax.add_artist(ab_text_lisere_1)


text_lisere_1 = TextArea(str(round(joueur_E3PTS*100,)) + '%', textprops=dict(color="k", size=20, ha='left',va='baseline', weight = 'bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.87, 0.56), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Team : " + str(round(equipe_E3PTS*100,)) + '%', textprops=dict(color="k", size=20, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.87, 0.54), frameon = False)
ax.add_artist(ab_text_lisere_1)




""" ____________ Contenu liseré gauche ________________________ """

text_lisere_1 = TextArea("PROGRAM", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.16, 0.50), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("- Player Stats", textprops=dict(color="k", size=25, ha='left',va='baseline', weight = 'normal'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.17, 0.40), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='normal'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.35), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Impact", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='normal'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.145, 0.32), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='normal'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.065, 0.335), frameon = False)
ax.add_artist(ab_text_lisere_1)


text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.27), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Efficiency", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.165, 0.24), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.065, 0.255), frameon = False)
ax.add_artist(ab_text_lisere_1)







"""______________________  Sauvegarde image ________________________________"""

output_path = 'Match_'+ str(numero_match) +'/'+ joueur_analyse +'_page_4.png'
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