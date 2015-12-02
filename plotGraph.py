#####################################################
##      Created on Nov 3, 2015 by Ailing Zhang     ##
#####################################################

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# plotGraph is used to plot the Markov process based on the Q matrix.

def plotGraph(res, name):
    G = nx.Graph(data=res)
    nx.draw(G)
    plt.savefig(name + ".png")
