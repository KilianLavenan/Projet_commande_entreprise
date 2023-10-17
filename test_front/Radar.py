# imports
import numpy as np
import matplotlib.pyplot as plt
import pygal
# may need to install CairoSVG with pygal

def vue_radar(pareto):
    dimensions=len(pareto[0])
    # data
    categories = ["Critère{i}" for i in range(1,dimensions+1)]
    #to close the radar shape add the first list element to the end of the list or concatenate
    for point in pareto:
        point.concatenate(point,[point[0]])
    label_placement = np.linspace(start=0, stop=2*np.pi, num=dimensions+1)
    # create matplotlib figure and polar plot with labels, title, and legend
    plt.figure(figsize=(6,6))
    plt.subplot(polar=True)
    for point in pareto:
        plt.plot(label_placement,point)
    lines, labels = plt.thetagrids(np.degrees(label_placement), labels=categories)
    plt.title('Compare pareto front Point', y=1.1, fontdict={'fontsize': 18})
    plt.legend(labels=["Point{i}" for i in range(len(pareto))],loc=(0.95, 0.8))
    plt.show()
