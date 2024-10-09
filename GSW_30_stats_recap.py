# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:13:25 2023

@author: jerem
"""

exec(open(debut_fichier+"background_top.py").read())


""" __________ STATS DU JOUEUR POUR LE MATCH ______________________________ """

Title_box = TextArea(joueur_analyse +' stats (G.' + str(numero_match) +')', 
                  textprops=dict(color="k", size=45, ha='left',va='baseline', weight ='bold'))
ab_Title_box = AnnotationBbox(Title_box, (0.5, 0.63), frameon = False)
ax.add_artist(ab_Title_box)


""" POINTS """
PTS_box = TextArea('PTS', 
                 textprops=dict(color="k", size=35, ha='left',va='baseline'))
ab_opponent_score = AnnotationBbox(PTS_box, (0.53, 0.45), frameon = False)
ax.add_artist(ab_opponent_score)

pts_box_1 = TextArea(joueur_pts, 
                 textprops=dict(color="k", size=35, ha='left',va='baseline', weight ='bold'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.42, 0.45), frameon = False)
ax.add_artist(ab_pts_box_1)

pts_box_1 = TextArea('Avg :' + str(joueur_pts_mean), 
                 textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.475, 0.42), frameon = False)
ax.add_artist(ab_pts_box_1)


""" REBONDS """

REB_box = TextArea('REB', 
                 textprops=dict(color="k", size=35, ha='left',va='baseline'))
ab_REB_box = AnnotationBbox(REB_box, (0.91, 0.45), frameon = False)
ax.add_artist(ab_REB_box)

reb_box_2 = TextArea(joueur_reb, 
                 textprops=dict(color="k", size=35, ha='left',va='baseline', weight ='bold'))
ab_reb_box_2 = AnnotationBbox(reb_box_2, (0.8, 0.45), frameon = False)
ax.add_artist(ab_reb_box_2)

pts_box_1 = TextArea('Avg :' + str(joueur_reb_mean), 
                 textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.855, 0.42), frameon = False)
ax.add_artist(ab_pts_box_1)


""" AST """
AST_box = TextArea('AST', 
                 textprops=dict(color="k", size=35, ha='left',va='baseline'))
ab_AST_box = AnnotationBbox(AST_box, (0.53, 0.35), frameon = False)
ax.add_artist(ab_AST_box)

ast_box_2 = TextArea(joueur_ast, 
                 textprops=dict(color="k", size=35, ha='left',va='baseline', weight ='bold'))
ab_ast_box_2 = AnnotationBbox(ast_box_2, (0.42, 0.35), frameon = False)
ax.add_artist(ab_ast_box_2)

pts_box_1 = TextArea('Avg :' + str(joueur_ast_mean), 
                 textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.475, 0.32), frameon = False)
ax.add_artist(ab_pts_box_1)


""" STL """
STL_box = TextArea('STL', 
                 textprops=dict(color="k", size=35, ha='left',va='baseline'))
ab_STL_box = AnnotationBbox(STL_box, (0.91, 0.35), frameon = False)
ax.add_artist(ab_STL_box)

stl_box_2 = TextArea(joueur_stl, 
                 textprops=dict(color="k", size=35, ha='left',va='baseline', weight ='bold'))
ab_stl_box_2 = AnnotationBbox(stl_box_2, (0.8, 0.35), frameon = False)
ax.add_artist(ab_stl_box_2)

pts_box_1 = TextArea('Avg :' + str(joueur_stl_mean), 
                 textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.855, 0.32), frameon = False)
ax.add_artist(ab_pts_box_1)


""" MINUTES """


MIN_box = TextArea('MIN', 
                 textprops=dict(color="k", size=35, ha='left',va='baseline'))
ab_MIN_box = AnnotationBbox(MIN_box, (0.53, 0.25), frameon = False)
ax.add_artist(ab_MIN_box)

min_box_2 = TextArea(joueur_min, 
                 textprops=dict(color="k", size=35, ha='left',va='baseline', weight ='bold'))
ab_min_box_2 = AnnotationBbox(min_box_2, (0.42, 0.25), frameon = False)
ax.add_artist(ab_min_box_2)

pts_box_1 = TextArea('Avg :' + str(joueur_min_mean), 
                 textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.475, 0.22), frameon = False)
ax.add_artist(ab_pts_box_1)



""" BLOCKS """


BLK_box = TextArea('BLK', 
                 textprops=dict(color="k", size=35, ha='left',va='baseline'))
ab_BLK_box = AnnotationBbox(BLK_box, (0.91, 0.25), frameon = False)
ax.add_artist(ab_BLK_box)

blk_box_2 = TextArea(joueur_blk, 
                 textprops=dict(color="k", size=35, ha='left',va='baseline', weight ='bold'))
ab_blk_box_2 = AnnotationBbox(blk_box_2, (0.8, 0.25), frameon = False)
ax.add_artist(ab_blk_box_2)

pts_box_1 = TextArea('Avg :' + str(joueur_blk_mean), 
                 textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_pts_box_1 = AnnotationBbox(pts_box_1, (0.855, 0.22), frameon = False)
ax.add_artist(ab_pts_box_1)


""" trait de séparation """

file_0 =image.imread('images/dark_trait_v.png')
imagebox = OffsetImage(file_0, zoom = 1)
ab_image = AnnotationBbox(imagebox, (0.3, 0.35), frameon = False)
ax.add_artist(ab_image)


""" ____________ Contenu liseré gauche ________________________ """

text_lisere_1 = TextArea("PROGRAM", textprops=dict(color="k", size=25, ha='left',va='baseline', weight ='bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.16, 0.50), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("- Player Stats", textprops=dict(color="k", size=25, ha='left',va='baseline', weight = 'bold'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.17, 0.40), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Player", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.135, 0.35), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("Impact", textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_text_lisere_1 = AnnotationBbox(text_lisere_1, (0.145, 0.32), frameon = False)
ax.add_artist(ab_text_lisere_1)

text_lisere_1 = TextArea("-", textprops=dict(color="k", size=25, ha='left',va='baseline'))
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


"""_______________________ flèches performances _____________________________ """

if diff_pts > 0 :
    file_0 =image.imread('images/fleche_verte.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.33, 0.46), frameon = False)
    ax.add_artist(ab_image)
elif diff_pts < 0 :
    file_0 =image.imread('images/fleche_rouge.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.33, 0.46), frameon = False)
    ax.add_artist(ab_image)
    
    
if diff_ast > 0 :
    file_0 =image.imread('images/fleche_verte.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.33, 0.36), frameon = False)
    ax.add_artist(ab_image)
elif diff_ast < 0 :
    file_0 =image.imread('images/fleche_rouge.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.33, 0.36), frameon = False)
    ax.add_artist(ab_image)
    
    
if diff_min > 0 :
    file_0 =image.imread('images/fleche_verte.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.33, 0.26), frameon = False)
    ax.add_artist(ab_image)
elif diff_min < 0 :
    file_0 =image.imread('images/fleche_rouge.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.33, 0.26), frameon = False)
    ax.add_artist(ab_image)
    
    
if diff_reb > 0 :
    file_0 =image.imread('images/fleche_verte.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.7, 0.46), frameon = False)
    ax.add_artist(ab_image)
elif diff_reb < 0 :
    file_0 =image.imread('images/fleche_rouge.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.7, 0.46), frameon = False)
    ax.add_artist(ab_image)
    
if diff_stl > 0 :
    file_0 =image.imread('images/fleche_verte.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.7, 0.36), frameon = False)
    ax.add_artist(ab_image)
elif diff_stl < 0 :
    file_0 =image.imread('images/fleche_rouge.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.7, 0.36), frameon = False)
    ax.add_artist(ab_image)


if diff_blk > 0 :
    file_0 =image.imread('images/fleche_verte.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.7, 0.26), frameon = False)
    ax.add_artist(ab_image)
elif diff_blk < 0 :
    file_0 =image.imread('images/fleche_rouge.png')
    imagebox = OffsetImage(file_0, zoom = 1)
    ab_image = AnnotationBbox(imagebox, (0.7, 0.26), frameon = False)
    ax.add_artist(ab_image)



# """_______________________ cheveron _____________________________ """

# file_0 =image.imread('images/chevron.png')
# imagebox = OffsetImage(file_0, zoom = 0.1)
# ab_image = AnnotationBbox(imagebox, (0.95, 0.03), frameon = False)
# ax.add_artist(ab_image)



"""______________________  Sauvegarde image ________________________________"""

output_path = 'Match_'+ str(numero_match) +'/'+ joueur_analyse +'_page_2.png'
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