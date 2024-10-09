# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:46:49 2023

@author: JVILLE
"""


"""_______________________ Stacked bar chart _______________________________"""

import matplotlib.pyplot as plt

couleur1 = ['#1D428A','#C4CED4', '#00471B', '#0E2240'] # [GSW, SAS, MIL, DEN]
couleur2 = ['#FFC72C', '#000000','#EEE1C6','#FEC524'] # [GSW, SAS, MIL, DEN]
indice_couleur = 3

#selecteur couleur : https://htmlcolorcodes.com/fr/ OU https://teamcolorcodes.com/denver-nuggets-color-codes/


# Data
categories = ['Category 1', 'Category 2', 'Category 3']
values1 = [6, 35, 24]
values2 = [5, 22, 23]

# Create stacked bar chart
fig, ax = plt.subplots()
ax.bar(categories, values1, label='Value 1', color=couleur1[indice_couleur])
ax.bar(categories, values2, bottom=values1, label='Value 2', color=couleur2[indice_couleur])

# Set chart labels and legend
font = {'family': 'sans serif', #arial, sans-serif, candara
        'weight': 'heavy',
        'size': 15,
        }

#    Add annotation values
for i, v1, v2 in zip(range(len(categories)), values1, values2):
        ax.text(i, v1/2, str(v1), ha='center', va='center', color=couleur2[indice_couleur], fontdict=font)
        ax.text(i, v1+v2/2, str(v2), ha='center',va='center', color=couleur1[indice_couleur], fontdict=font)

ax.legend()

# Remove background color
ax.set_facecolor('none')
fig.set_facecolor('none')

# Show the chart
plt.show()




# """_______________________ Double bar chart _______________________________"""


# import numpy as np  
# import matplotlib.pyplot as plt  
  
# SA1 = '#839192' 
# SA2 = '#D7DBDD'

# #selecteur couleur : https://htmlcolorcodes.com/fr/


# # Data
# categories = ['Category 1', 'Category 2', 'Category 3']
# values1 = [6, 35, 34]
# values2 = [5, 22, 23]


  
# X_axis = np.arange(len(categories)) 


# # Set chart labels and legend
# font = {'family': 'sans-serif',
#         'color':  '#212F3D',
#         'weight': 'bold',
#         'size': 15,
#         }

# opacity = 1
  
# plt.bar(X_axis - 0.2, values1, 0.4, color=SA1,alpha=opacity, label='Attempted')

# for i, v in enumerate(values1):
#     plt.text(i - 0.2, v/2, str(v), ha='center', va='center', fontdict=font)

# plt.bar(X_axis + 0.2, values2, 0.4, color=SA2, alpha=opacity, label='Scored')

# for i, v in enumerate(values2):
#     plt.text(i + 0.2, v/2, str(v), ha='center', va='center', fontdict=font)
  
# plt.xticks(X_axis, categories) 

# plt.legend() 

# plt.show()