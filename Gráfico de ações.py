# -*- coding: utf-8 -*-
"""
Created on Thu May  5 20:54:06 2022

@author: Everton SSD
"""

import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
#import numpy as np
import matplotlib.patches as mpatches
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 17,
        }
Ano = 295
SeisMeses = 338
TresMeses = 204
UmMes = 211
UmaSemana =187
Hoje = 194
fig, ax = plt.subplots(figsize =(10,7))
y = [Ano, SeisMeses, TresMeses, UmMes, UmaSemana, Hoje]
x = ['Ano', '6 Meses', '3 Meses', ' 1 Mês', '1 Semana', 'Hoje']
plt.plot(x, y,  marker = 'o' , color = '#4CAF50', linewidth = '2.5')
linha = mpatches.Patch(color='green', label='Linha das ações', linewidth = '2.5')
#Posso traçar outro traço também utilizando a função plt.plot, podendo ser 2 ou mais
#plt.plot(y, marker = 'o', color = 'r', linewidth = '2.5')
#plt.plot(x, marker = 'o', color = 'r', linewidth = '2.5')
for x1, y1 in zip(x,y):
    ax.text(x1, y1 +2, y1)
plt.grid(axis = 'x', linestyle = '--')
plt.title("Cotação do Bitcoin", fontdict = font , loc = 'Center', color ='orange')
plt.xlabel("Tempo", fontdict = font, color = 'Black')
plt.ylabel("Valor das Ações", fontdict = font, color = 'Black')


ax.legend(handles=[linha], loc='upper right')
plt.show()