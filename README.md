# NBA_data_analyst
Projet python qui permet de comparer les performances d'un joueur NBA sur un match par rapport à celle de son équipe.

A travers plusieurs visuels, l'utilisateur est capable de savoir si le joueur a sous-performé ou sur-performé pendant un match. L'efficacité du joueur est aussi mise en évidence. 
Il est aussi possible de connaître l'impact du joueur étudié sur les performances de son équipe.

Les insights mis en évidence pour les performances sont :
  - Nombre de points (Pendant le match et comparaison avec la moyenne de la saison)
  - Nombre de passes décisives (Pendant le match et comparaison avec la moyenne de la saison)
  - Nombre de minutes jouées (Pendant le match et comparaison avec la moyenne de la saison)
  - Nombre de rebonds offensifs et défensifs (Pendant le match et comparaison avec la moyenne de la saison)
  - Nombre d'interceptions (Pendant le match et comparaison avec la moyenne de la saison)
  - Nombre de contres (Pendant le match et comparaison avec la moyenne de la saison)
Chacun de ces insights sera caractérisés par une flèche rouge ou verte si la performance du match est plus ou moins bonne que la moyenne.

Les insights mis en évidence pour l'impact du joueur dans son équipe sont identifés dans un radar chart :
Ce radar compare 3 performances exprimées entre 0 et 1
  - Performances de l'équipe. Elles représentent le maximum possible (100%)
  - Performances du joueurs
  - Performances moyennes du joueurs
Les insights de ce radar sont les suivants :
  - Nombre total de rebonds (Total REB)
  - Temps joué (Time)
  - Interceptions (STL)
  - Contres (BLK)
  - Points inscrits (PTS)
  - Passes décisives délivrées (AST)
  - Nombre de rebonds défensifs (defensive REB)
  - Nombre de rebonds offensifs (offensive REB)


Les insights mis en évidence pour l'efficacité des tirs du joueur sont identifés dans un histogramme empilé :
Il y a 3 catégories de tirs :
  - 3 points (3P)
  - 2 points (FG)
  - Lancer-francs (FT)
Chaque catégorie compare le nombre de tirs tentés et réussis
Chaque catégorie compare le pourcentage de réussite du joueur par rapport à son équipe.

Bibliothèques utilisées :

pandas
matplotlib.pyplot
import matplotlib.image
matplotlib.offsetbox
datetime
matplotlib.patches
numpy
os
PIL
sys
email.message
ssl
smtplib


