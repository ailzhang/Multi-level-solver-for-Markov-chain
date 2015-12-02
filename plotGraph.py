#####################################################
##      Created on Nov 3, 2015 by Ailing Zhang     ##
#####################################################

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def plotGraph(res, name):
    G = nx.Graph(data=res)
    nx.draw(G)
    plt.savefig(name + ".png")
