# imports
import math
import numpy as np
import matplotlib.pyplot as plt
import pygal
# may need to install CairoSVG with pygal

def to_liste1(pareto):
    pareto=pareto.tolist()
    return pareto

def to_liste2(pareto):
    pareto=list(pareto)
    for i in range(len(pareto)):
        pareto[i]=list(pareto[i])
    return pareto

def vue_radar(pareto):
    pareto=to_liste2(pareto)
    print(pareto)
    # data
    categories = [f"Critère {i}" for i in range(1,len(pareto[0])+1)]
    categories.append("Critère 1")
    #to close the radar shape add the first list element to the end of the list or concatenate
    for point in pareto:
        point.append(point[0])
    label_placement = np.linspace(start=0, stop=2*np.pi, num=len(pareto[0]))
    # create matplotlib figure and polar plot with labels, title, and legend
    fig=plt.figure(figsize=(8,8))
    point_sublists = [pareto[i:min(i + 5,len(pareto)-1)] for i in range(0, len(pareto), 5)]
    i=1
    for sublist in point_sublists:
    # Le nombre de colonnes dans la figure (1 pour une seule colonne)
        num_rows = 1
    
    # Calculez le nombre de lignes en fonction du nombre de sous-plots par colonne
        num_cols = len(point_sublists) // num_rows + (len(point_sublists) % num_rows > 0)
        ax = fig.add_subplot(num_rows, num_cols, i,polar=True)
        i+=1
        lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categories)
        for point in sublist:
            ax.plot(label_placement,point)
        ax.legend(labels=[f"Point{(i-2)*5+j+1}" for j in range(len(sublist))],loc='lower right',fontsize=5)
    fig.suptitle('Compare pareto front Point', fontsize= 22)
    plt.show()
