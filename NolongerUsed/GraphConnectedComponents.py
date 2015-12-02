#####################################################
##      Created on Nov 30, 2015 by Ailing Zhang     ##
#####################################################
import pdb
import networkx as nx
import numpy as np
from BlockedMatrix import BlockedMatrix

def GraphPartitionByConnectedComponent(P):
    G = nx.Graph(data = P)
    connected = nx.connected_components(G)
    cluster = [list(i) for i in list(connected)]
    return cluster


if __name__ == "__main__":
    pdb.set_trace()
    test = BlockedMatrix(20,4)
    print GraphPartition(test)
