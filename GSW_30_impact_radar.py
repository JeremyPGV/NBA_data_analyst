# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:05:05 2023

@author: jerem
"""


""" ---------------  CREATION GRAPHIQUE -------------------------- """

categories = ['Time', 'Total REB', 'Offensive REB ', 'Defensive REB',
              'AST', 'PTS', 'BLK', 'STL', 'Time']

stats_joueur_mean = [prcg_time_played_mean, prcg_total_reb_mean, prcg_oreb_mean, prcg_dreb_mean, 
                prcg_ast_mean, prcg_pts_mean, prcg_blk_mean, prcg_stl_mean]
stats_joueur_mean = np.concatenate((stats_joueur_mean, [stats_joueur_mean[0]]))


stats_joueur = [prcg_time_played, prcg_total_reb, prcg_oreb, prcg_dreb, 
                prcg_ast, prcg_pts, prcg_blk, prcg_stl]
stats_joueur = np.concatenate((stats_joueur, [stats_joueur[0]]))


stats_equipe = [1, 1, 1, 1, 1, 1, 1,1]
stats_equipe = np.concatenate((stats_equipe, [stats_equipe[0]]))



# calculate evenly-spaced angle coordinates
label_placement = np.linspace(start=0, stop=2 * np.pi, num=len(stats_joueur))

# create matplotlib figure and polar plot with labels, title, and legend
plt.figure(figsize=(5.25, 5.25))
plt.subplot(polar=True)

# Fill the radar plots
plt.fill(label_placement, stats_joueur, color=couleur1[indice_couleur], alpha=0.2) #bleu
plt.fill(label_placement, stats_equipe, color=couleur2[indice_couleur], alpha=0.2) #jaune
plt.fill(label_placement, stats_joueur_mean, 'red', alpha=0.2)

# Plot the lines on top of the filled areas
plt.plot(label_placement, stats_joueur, color=couleur1[indice_couleur]) #bleu
plt.plot(label_placement, stats_equipe, color=couleur2[indice_couleur]) #jaune
plt.plot(label_placement, stats_joueur_mean, 'red')


# use thetagrids to place labels at the specified angles using degrees
lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categories)
#plt.title('Compare Vehicles', y=1.1, fontdict={'fontsize': 18})
plt.legend(labels=['Player', equipe_domicile,'Player avg.'], loc=(0.8, 0.95))

output_path = 'Match_' + str(numero_match) +'/'+ joueur_analyse + '_page_3.png'
plt.savefig(output_path, bbox_inches='tight', pad_inches=0, transparent=True)




exec(open(debut_fichier+"background_top.py").read())



legend_box_graph = TextArea(joueur_analyse + ' impact (G.' + str(numero_match) +')', 
                  textprops=dict(color="k", size=45, ha='left',va='baseline', weight ='bold'))
ab_legend = AnnotationBbox(legend_box_graph, (0.5, 0.63), frameon = False)
ax.add_artist(ab_legend)



file=image.imread('Match_' + str(numero_match) +'/'+ joueur_analyse + '_page_3.png')
imagebox = OffsetImage(file, zoom = 1.45)
ab_file = AnnotationBbox(imagebox, (0.64, 0.33), frameon = False)
ax.add_artist(ab_file)

# """_______________________ cheveron _____________________________ """

# file_0 =image.imread('images/chevron.png')
# imagebox = OffsetImage(file_0, zoom = 0.1)
# ab_image = AnnotationBbox(imagebox, (0.95, 0.03), frameon = False)
# ax.add_artist(ab_image)



"""_______________________ Trait vertical _____________________________ """

file_0 =image.imread('images/dark_trait_v.png')
imagebox = OffsetImage(file_0, zoom = 1)
ab_image = AnnotationBbox(imagebox, (0.3, 0.35), frameon = False)
ax.add_artist(ab_image)


""" ____________ Contenu liseré gauche ________________________ """

text_lisere_1 = TextArea("PROGRAM", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.16, 0.50), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("- Player Stats", textprops=dict(color="k", size=25, ha='left',va='baseline', weight = 'normal'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.17, 0.40), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.35), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Impact", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.145, 0.32), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.065, 0.335), frameon = False)
ax.add_artist(ab_text_lisere_1)


text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.27), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Efficiency", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.16, 0.24), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.065, 0.255), frameon = False)
ax.add_artist(ab_text_lisere_1)


"""______________________  Sauvegarde image ________________________________"""

output_path = 'Match_'+ str(numero_match) +'/'+ joueur_analyse +'_page_3.png'
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