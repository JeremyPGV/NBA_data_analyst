# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 07:09:28 2023

@author: jerem
"""


""" _____________ MERGE des 2 DFs  ___________________"""

dataframe_merge = pd.merge (dataframe, dataframe_equipe, 
                            left_on = dataframe.columns[0], 
                            right_on = dataframe_equipe.columns[0])


""" _____________ n° match, equipe domicile, adversaire  ___________________"""


numero_match = len(dataframe_equipe) #on prend le nombre de match joué par l'equipe
print ("C'est le match #",numero_match)


valeur_cellule_indiv_1 = dataframe_merge.iloc[0, 0]  # 0 correspond à la première ligne, 2 correspond à la troisième colonne (0-indexed)

adversaire = valeur_cellule_indiv_1[-3:]
print ("L'adversaire est ",adversaire)

equipe_domicile = valeur_cellule_indiv_1[15:18]
print ("L'equipe a domicile est ",equipe_domicile)


""" ____________________score domicile _________________________________ """
score_domicile = dataframe_merge.iloc[0, 25]
print ("Le score de l'equipe a domicile est ",score_domicile)


""" ____________________score adversaire _________________________________ """

score_adversaire = score_domicile - dataframe_merge.iloc[0, 43]
print ("Le score de l'adversaire est ",score_adversaire)

""" ______________ Nombre de points inscrits (joueur) ____________________"""

joueur_pts = int(dataframe_merge.iloc[0, 3])
print (joueur_analyse + " a inscrit ",joueur_pts, "points")


""" ______________ Nombre de rebonds inscrits (joueur) ____________________"""

joueur_oreb = int(dataframe_merge.iloc[0, 13])
joueur_dreb = int(dataframe_merge.iloc[0, 14])
joueur_reb = joueur_oreb + joueur_dreb
print (joueur_analyse + " a inscrit ",joueur_reb, "rebonds")


""" ______________ Nombre de passes inscrits (joueur) ____________________"""

joueur_ast = int(dataframe_merge.iloc[0, 16])
print (joueur_analyse + " a inscrit ",joueur_ast, "passes")


""" ______________ Nombre de interceptions inscrites (joueur) ____________"""

joueur_stl = int(dataframe_merge.iloc[0,17])
print (joueur_analyse + " a fait ",joueur_stl, "interceptions")

""" ______________ Nombre de minutes jouées (joueur) ____________"""

joueur_min = int(dataframe_merge.iloc[0,2])
print (joueur_analyse + " a joue ",joueur_min, "minutes")


""" ______________ Nombre de bloc réalisé (joueur) ____________"""

joueur_blk = int(dataframe_merge.iloc[0,18])
print (joueur_analyse + " a fait ",joueur_blk, "block")



"""______________________ Nombre de 2 points inscrits (joueur)___________"""
joueur_FGM = int(dataframe_merge.iloc[0,4])
print (joueur_analyse + " a fait ",joueur_FGM, "FGM")


"""______________________ Nombre de 2 points tenté (joueur)___________"""
joueur_FGA = int(dataframe_merge.iloc[0,5])
print (joueur_analyse + " a fait ",joueur_FGA, "FGA")


"""______________________ Nombre de 3 points inscrits (joueur)___________"""
joueur_3PM = int(dataframe_merge.iloc[0,7])
print (joueur_analyse + " a fait ",joueur_3PM, "3PM")


"""______________________ Nombre de 3 points tenté (joueur)___________"""
joueur_3PA = int(dataframe_merge.iloc[0,8])
print (joueur_analyse + " a fait ",joueur_3PA, "3PA")


"""______________________ Nombre de lancé-franc inscrits (joueur)___________"""
joueur_FTM = int(dataframe_merge.iloc[0,10])
print (joueur_analyse + " a fait ",joueur_FTM, "FTM")


"""______________________ Nombre de lancé-franc tentés (joueur)___________"""
joueur_FTA = int(dataframe_merge.iloc[0,11])
print (joueur_analyse + " a fait ",joueur_FTA, "FTA")

"""______________________ Efficacité 2PTS (joueur)___________"""
joueur_E2PTS = int(dataframe_merge.iloc[0,6])/100
print (joueur_analyse + " a une efficacité de  ",joueur_E2PTS, "à 2 points")

"""______________________ Efficacité 3PTS (joueur)___________"""
joueur_E3PTS = int(dataframe_merge.iloc[0,9])/100
print (joueur_analyse + " a une efficacité de  ",joueur_E3PTS, "à 3 points")

"""______________________ Efficacité FT (joueur)___________"""
joueur_EFT = int(dataframe_merge.iloc[0,12])/100
print (joueur_analyse + " a une efficacité de  ",joueur_EFT, "au FT")

""" ----------------------------------------------------------------------"""


""" ______________ Nombre de minutes jouées (équipe) ____________"""

equipe_min = int(dataframe_merge.iloc[0,24])
print (equipe_analyse + " a joue ",equipe_min, "minutes")


""" ______________ Nombre de rebonds inscrits (équipe) ____________________"""

equipe_oreb = int(dataframe_merge.iloc[0, 35])
equipe_dreb = int(dataframe_merge.iloc[0, 36])
equipe_reb = equipe_oreb + equipe_dreb
print (equipe_analyse + " a inscrit ",equipe_reb, "rebonds")


""" ______________ Nombre de passes faites (équipe) ____________"""

equipe_ast = int(dataframe_merge.iloc[0,38])
print (equipe_analyse + " a fait ",equipe_ast, "passes")



""" ______________ Nombre de stl faites (équipe) ____________"""

equipe_stl = int(dataframe_merge.iloc[0,40])
print (equipe_analyse + " a fait ",equipe_stl, "STL")



""" ______________ Nombre de BLK faits (équipe) ____________"""

equipe_blk = int(dataframe_merge.iloc[0,41])
print (equipe_analyse + " a fait ",equipe_blk, "BLK")



"""______________________ Efficacité 2PTS (équipe)___________"""
equipe_E2PTS = int(dataframe_merge.iloc[0,28])/100
print (equipe_analyse + " a une efficacité de  ",equipe_E2PTS, "à 2 points")


"""______________________ Efficacité 3PTS (équipe)___________"""
equipe_E3PTS = int(dataframe_merge.iloc[0,31])/100
print (equipe_analyse + " a une efficacité de  ",equipe_E3PTS, "à 3 points")


"""______________________ Efficacité FT (équipe)___________"""
equipe_EFT = int(dataframe_merge.iloc[0,34])/100
print (equipe_analyse + " a une efficacité de  ",equipe_EFT, "au FT")


"""______________________ Série victoire/défaite (équipe)___________"""

serie_defaite_equipe_domicile = dataframe_equipe.iloc[:, 1].str.count('L').sum()

serie_victoire_equipe_domicile = dataframe_equipe.iloc[:, 1].str.count('W').sum()


"""______________________ Stats joueur matchs précédents ___________________"""


joueur_pts_mean = round(dataframe_merge.iloc[1:, 3].mean(),)

joueur_oreb_mean = round(dataframe_merge.iloc[1:, 13].mean(),)

joueur_dreb_mean = round(dataframe_merge.iloc[1:, 14].mean(),)

joueur_reb_mean = round(dataframe_merge.iloc[1:, 15].mean(),)

joueur_ast_mean = round(dataframe_merge.iloc[1:, 16].mean(),)

joueur_stl_mean = round(dataframe_merge.iloc[1:, 17].mean(),)

joueur_min_mean = round(dataframe_merge.iloc[1:, 2].mean(),)

joueur_blk_mean = round(dataframe_merge.iloc[1:, 18].mean(),)


"""______________________ Diff Stats joueur vs matchs précédents ___________"""


diff_pts = round (joueur_pts - joueur_pts_mean,)

diff_reb = round (joueur_reb - joueur_reb_mean,)

diff_ast = round (joueur_ast - joueur_ast_mean,)

diff_stl = round (joueur_stl - joueur_stl_mean,)

diff_min = round (joueur_min - joueur_min_mean,)

diff_blk = round (joueur_blk - joueur_blk_mean,)


"""______________________ Stats équipe matchs précédents ___________________"""


equipe_pts_mean = round(dataframe_merge.iloc[1:, 25].mean(),)

equipe_oreb_mean = round(dataframe_merge.iloc[1:, 35].mean(),)

equipe_dreb_mean = round(dataframe_merge.iloc[1:, 36].mean(),)

equipe_reb_mean = round(dataframe_merge.iloc[1:, 37].mean(),)

equipe_ast_mean = round(dataframe_merge.iloc[1:, 38].mean(),)

equipe_stl_mean = round(dataframe_merge.iloc[1:, 40].mean(),)

equipe_min_mean = round(dataframe_merge.iloc[1:, 24].mean(),)

equipe_blk_mean = round(dataframe_merge.iloc[1:, 41].mean(),)


""" ---------------  CALCUL DES POURCENTAGES Match actuel------------------ """

prcg_time_played = round(joueur_min/equipe_min,1)
prcg_total_reb = round(joueur_reb/equipe_reb,1)
prcg_oreb = round(joueur_oreb/equipe_oreb,1)
prcg_dreb = round(joueur_dreb/equipe_dreb,1)
prcg_ast = round(joueur_ast/equipe_ast,1)
prcg_pts = round(joueur_pts/score_domicile,1)
prcg_stl = round(joueur_stl/equipe_stl,1)
prcg_blk = round(joueur_blk/equipe_blk,1)


""" ---------------  CALCUL DES POURCENTAGES Match précédents ------------- """

prcg_time_played_mean = round(joueur_min_mean/equipe_min_mean,1)
prcg_total_reb_mean = round(joueur_reb_mean/equipe_reb_mean,1)
prcg_oreb_mean = round(joueur_oreb_mean/equipe_oreb_mean,1)
prcg_dreb_mean = round(joueur_dreb_mean/equipe_dreb_mean,1)
prcg_ast_mean = round(joueur_ast_mean/equipe_ast_mean,1)
prcg_pts_mean = round(joueur_pts_mean/equipe_pts_mean,1)
prcg_stl_mean = round(joueur_stl_mean/equipe_stl_mean,1)
prcg_blk_mean = round(joueur_blk_mean/equipe_blk_mean,1)













