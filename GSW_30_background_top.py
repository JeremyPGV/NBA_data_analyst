# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:36:03 2023

@author: jerem
"""

"""_____________ IMAGE DE FOND -- ARRIERE PLAN______________________________"""

fig = plt.figure(figsize=(10.8, 13.8), dpi=100, facecolor = arrier_plan)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')


file_0 =image.imread('images/'+debut_fichier+'bg.png')
imagebox = OffsetImage(file_0, zoom = 0.7105)
ab_image = AnnotationBbox(imagebox, (0.5, 0.5), frameon = False)
ax.add_artist(ab_image)



"""_____________ Entete - FICHE joueur ______________________________"""

file_0 =image.imread('images/dark_entete.png')
imagebox = OffsetImage(file_0, zoom = 0.7105)
ab_image = AnnotationBbox(imagebox, (0.5, 0.87), frameon = False)
ax.add_artist(ab_image)

file_0 =image.imread('images/'+ debut_fichier +'img.png')
imagebox = OffsetImage(file_0, zoom = 0.38)
ab_image = AnnotationBbox(imagebox, (0.25, 0.85), frameon = False)
ax.add_artist(ab_image)

player_name = TextArea(joueur_analyse, textprops=dict(color="k", size=30, ha='left',va='baseline'))
ab_player_name = AnnotationBbox(player_name, (0.75, 0.93), frameon = False)
ax.add_artist(ab_player_name)

player_detail = TextArea(joueur_nbr_post, textprops=dict(color="k", size=30, ha='left',va='baseline'))
ab_player_detail = AnnotationBbox(player_detail, (0.75, 0.895), frameon = False)
ax.add_artist(ab_player_detail)


match_str = TextArea("Game "+ str(numero_match) , textprops=dict(color="k", size=30, ha='left',va='baseline'))
ab_match_str = AnnotationBbox(match_str, (0.75, 0.86), frameon = False)
ax.add_artist(ab_match_str)


season_detail = TextArea(saison, textprops=dict(color="k", size=30, ha='left',va='baseline'))
ab_season_detail = AnnotationBbox(season_detail, (0.75, 0.80), frameon = False)
ax.add_artist(ab_season_detail)

season_year = TextArea(annee, textprops=dict(color="k", size=25, ha='left',va='baseline'))
ab_season_year = AnnotationBbox(season_year, (0.75, 0.77), frameon = False)
ax.add_artist(ab_season_year)



"""_____________ TEAMS logo & boxscores ______________________________"""


""" Equipe domicile """

if equipe_domicile == 'ATL' :
    zoom_equipe_domicile = 0.09
    couleur_texte = "r"
elif equipe_domicile == 'BOS' :
    zoom_equipe_domicile = 0.095
    couleur_texte = "w"
elif equipe_domicile == 'BKN' :
    zoom_equipe_domicile = 0.01
    couleur_texte = "w"
elif equipe_domicile == 'CHI' :
    zoom_equipe_domicile = 0.04
    couleur_texte = "r"
elif equipe_domicile == 'CHO' :
    zoom_equipe_domicile = 0.04
    couleur_texte = "b"
elif equipe_domicile == 'CLE' :
    zoom_equipe_domicile = 0.05
    couleur_texte = "y"
elif equipe_domicile == 'DAL' :
    zoom_equipe_domicile = 0.085
    couleur_texte = "w"
elif equipe_domicile == 'DEN' :
    zoom_equipe_domicile = 0.12
    couleur_texte = "b"
elif equipe_domicile == 'DET' :
    zoom_equipe_domicile = 0.4
    couleur_texte = "w"
elif equipe_domicile == 'HOU' :
    zoom_equipe_domicile = 0.4
    couleur_texte = "r"
elif equipe_domicile == 'LAC' :
    zoom_equipe_domicile = 0.4
    couleur_texte = "w"
elif equipe_domicile == 'LAL' :
    zoom_equipe_domicile = 0.25
    couleur_texte = "y"
elif equipe_domicile == 'MEM' :
    zoom_equipe_domicile = 0.45
    couleur_texte = "k"
elif equipe_domicile == 'MIA' :
    zoom_equipe_domicile = 0.5
    couleur_texte = "r"
elif equipe_domicile == 'MIL' : 
    zoom_equipe_domicile = 0.1
    couleur_texte = "w"
elif equipe_domicile == 'IND' :
    zoom_equipe_domicile = 0.04
    couleur_texte = "w"
elif equipe_domicile == 'MIN' :
    zoom_equipe_domicile = 0.38
    couleur_texte = "w"
elif equipe_domicile == 'NOP' :
    zoom_equipe_domicile = 0.3
    couleur_texte = "y"
elif equipe_domicile == 'NYK' :
    zoom_equipe_domicile = 0.35
    couleur_texte = "k"
elif equipe_domicile == 'OKC' :
    zoom_equipe_domicile = 0.45
    couleur_texte = "w"
elif equipe_domicile == 'ORL' :
    zoom_equipe_domicile = 0.305
    couleur_texte = "b"
elif equipe_domicile == 'PHI' :
    zoom_equipe_domicile = 0.29
    couleur_texte = "w"
elif equipe_domicile == 'PHX' :
    zoom_equipe_domicile = 0.41
    couleur_texte = "y"
elif equipe_domicile == 'POR' :
    zoom_equipe_domicile = 0.41
    couleur_texte = "w"
elif equipe_domicile == 'SAC' :
    zoom_equipe_domicile = 0.38
    couleur_texte = "k"
elif equipe_domicile == 'SAS' :
    zoom_equipe_domicile = 0.23
    couleur_texte = "k"
elif equipe_domicile == 'TOR' :
    zoom_equipe_domicile = 0.35
    couleur_texte = "r"
elif equipe_domicile == 'UTA' :
    zoom_equipe_domicile = 0.35
    couleur_texte = "b"
elif equipe_domicile == 'WAS' :
    zoom_equipe_domicile = 0.1
    couleur_texte = "b"
elif equipe_domicile == 'GSW' :
    zoom_equipe_domicile = 0.4
    couleur_texte = "b"

#else : zoom_equipe_domicile = 0.8

domicile_img = 'images/' + equipe_domicile +'-removebg-preview.png'
domicile_boxscore = 'images/' + equipe_domicile +'_boxscore.png'

file_0 =image.imread(domicile_boxscore)
imagebox = OffsetImage(file_0, zoom = 1)
ab_image = AnnotationBbox(imagebox, (0.255, 0.715), frameon = False)
ax.add_artist(ab_image)

file_0 =image.imread(domicile_img)
imagebox = OffsetImage(file_0, zoom = zoom_equipe_domicile)
ab_image = AnnotationBbox(imagebox, (0.08, 0.715), frameon = False)
ax.add_artist(ab_image)

home_team = TextArea(equipe_domicile, textprops=dict(color=couleur_texte, size=30, ha='left',va='baseline'))
ab_home_team = AnnotationBbox(home_team, (0.3, 0.715), frameon = False)
ax.add_artist(ab_home_team)

home_score = TextArea(str(score_domicile), textprops=dict(color=couleur_texte, size=30, ha='left',va='baseline', weight ='bold'))
ab_home_score = AnnotationBbox(home_score, (0.43, 0.715), frameon = False)
ax.add_artist(ab_home_score)

home_serie = TextArea(str(serie_victoire_equipe_domicile)+" - "
                       + str(serie_defaite_equipe_domicile), textprops=dict(color=couleur_texte, size=20, ha='left',va='baseline'))
ab_home_serie = AnnotationBbox(home_serie, (0.17, 0.715), frameon = False)
ax.add_artist(ab_home_serie)



""" Equipe extérieure """


if adversaire == 'ATL' :
    zoom_adversaire = 0.09
    couleur_texte = "r"
elif adversaire == 'BOS' :
    zoom_adversaire = 0.095
    couleur_texte = "w"
elif adversaire == 'BKN' :
    zoom_adversaire = 0.01
    couleur_texte = "w"
elif adversaire == 'CHI' :
    zoom_adversaire = 0.04
    couleur_texte = "r"
elif adversaire == 'CHO' :
    zoom_adversaire = 0.04
    couleur_texte = "b"
elif adversaire == 'CLE' :
    zoom_adversaire = 0.05
    couleur_texte = "y"
elif adversaire == 'DAL' :
    zoom_adversaire = 0.085
    couleur_texte = "w"
elif adversaire == 'DEN' :
    zoom_adversaire = 0.12
    couleur_texte = "b"
elif adversaire == 'DET' :
    zoom_adversaire = 0.4
    couleur_texte = "w"
elif adversaire == 'HOU' :
    zoom_adversaire = 0.4
    couleur_texte = "r"
elif adversaire == 'LAC' :
    zoom_adversaire = 0.4
    couleur_texte = "w"
elif adversaire == 'LAL' :
    zoom_adversaire = 0.25
    couleur_texte = "y"
elif adversaire == 'MEM' :
    zoom_adversaire = 0.45
    couleur_texte = "k"
elif adversaire == 'MIA' :
    zoom_adversaire = 0.5
    couleur_texte = "r"
elif adversaire == 'MIL' : 
    zoom_adversaire = 0.1
    couleur_texte = "w"
elif adversaire == 'IND' :
    zoom_adversaire = 0.04
    couleur_texte = "w"
elif adversaire == 'MIN' :
    zoom_adversaire = 0.38
    couleur_texte = "w"
elif adversaire == 'NOP' :
    zoom_adversaire = 0.3
    couleur_texte = "y"
elif adversaire == 'NYK' :
    zoom_adversaire = 0.35
    couleur_texte = "k"
elif adversaire == 'OKC' :
    zoom_adversaire = 0.45
    couleur_texte = "w"
elif adversaire == 'ORL' :
    zoom_adversaire = 0.305
    couleur_texte = "b"
elif adversaire == 'PHI' :
    zoom_adversaire = 0.29
    couleur_texte = "w"
elif adversaire == 'PHX' :
    zoom_adversaire = 0.41
    couleur_texte = "y"
elif adversaire == 'POR' :
    zoom_adversaire = 0.41
    couleur_texte = "r"
elif adversaire == 'SAC' :
    zoom_adversaire = 0.38
    couleur_texte = "k"
elif adversaire == 'SAS' :
    zoom_adversaire = 0.23
    couleur_texte = "k"
elif adversaire == 'TOR' :
    zoom_adversaire = 0.35
    couleur_texte = "r"
elif adversaire == 'UTA' :
    zoom_adversaire = 0.35
    couleur_texte = "b"
elif adversaire == 'WAS' :
    zoom_adversaire = 0.1
    couleur_texte = "b"
elif adversaire == 'GSW' :
    zoom_adversaire = 0.4
    couleur_texte = "b"

#else : zoom_equipe_domicile = 0.8

adversaire_img = 'images/' + adversaire +'-removebg-preview.png'
adversaire_boxscore = 'images/' + adversaire +'_boxscore.png'

file_0 =image.imread(adversaire_boxscore)
imagebox = OffsetImage(file_0, zoom = 1)
ab_image = AnnotationBbox(imagebox, (0.7465, 0.715), frameon = False)
ax.add_artist(ab_image)

file_0 =image.imread(adversaire_img)
imagebox = OffsetImage(file_0, zoom = zoom_adversaire)
ab_image = AnnotationBbox(imagebox, (0.92, 0.715), frameon = False)
ax.add_artist(ab_image)


visit_score = TextArea(str(score_adversaire), textprops=dict(color=couleur_texte, size=30, ha='left',va='baseline', weight ='bold'))
ab_visit_score = AnnotationBbox(visit_score, (0.57, 0.715), frameon = False)
ax.add_artist(ab_visit_score)


visit_team = TextArea(adversaire, textprops=dict(color=couleur_texte, size=30, ha='left',va='baseline'))
ab_visit_team = AnnotationBbox(visit_team, (0.70, 0.715), frameon = False)
ax.add_artist(ab_visit_team)


visit_serie = TextArea(str(serie_victoire_adversaire)+" - "
                       + str(serie_defaite_adversaire),textprops=dict(color=couleur_texte, size=20, ha='left',va='baseline'))
ab_visit_serie = AnnotationBbox(visit_serie, (0.83, 0.715), frameon = False)
ax.add_artist(ab_visit_serie)


"""_____________ Logo chaine  ______________________________"""

presented_by = TextArea("@nba_data_analyst",textprops=dict(color="k", size=35, ha='left',va='baseline',weight='bold'))
ab_presented_by = AnnotationBbox(presented_by, (0.5, 0.03), frameon = False)
ax.add_artist(ab_presented_by)





"""______________________  Sauvegarde image ________________________________"""

output_path = 'base_travail.png'
plt.savefig(output_path, bbox_inches='tight', pad_inches=0, transparent=False)

# output_path = 'Match_'+ str(numero_match) +'/'+ joueur_analyse +'_page_8.png'
# plt.savefig(output_path, bbox_inches='tight', pad_inches=0, transparent=False)


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