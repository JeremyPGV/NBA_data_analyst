# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:46:49 2023

@author: JVILLE
"""

import matplotlib.pyplot as plt
import random

SA1 = '#839192' 
SA2 = '#D7DBDD'

#selecteur couleur : https://htmlcolorcodes.com/fr/


# Data
categories = ['Category 1', 'Category 2', 'Category 3']
values1 = [6, 35, 4]
values2 = [5, 22, 23]

# Create stacked bar chart
fig, ax = plt.subplots()
ax.bar(categories, values1, label='Value 1', color=SA1)
ax.bar(categories, values2, bottom=values1, label='Value 2', color=SA2)

# Set chart labels and legend
font = {'family': 'sans-serif',
        'color':  '#212F3D',
        'weight': 'bold',
        'size': 15,
        }

#    Add annotation values
for i, v1, v2 in zip(range(len(categories)), values1, values2):
   # if v1 + v2 >= 6:
        ax.text(i, v1/2, str(v1), ha='center', va='center', fontdict=font)
        ax.text(i, v1+v2/2, str(v2), ha='center', va='center', fontdict=font)

ax.legend()

# Remove background color
ax.set_facecolor('none')
fig.set_facecolor('none')

# Show the chart
plt.show()