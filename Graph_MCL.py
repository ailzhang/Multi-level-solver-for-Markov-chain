#####################################################
##      Created on Nov 3, 2015 by Ailing Zhang     ##
#####################################################
import numpy as np
import networkx as nx
import pdb
from BlockedMatrix import BlockedMatrix
from plotGraph import plotGraph

def GraphPartitionByMCL(Q, exp=2, inf=2, max_loop=10):
    P = np.copy(Q)
    P = removeDiag(P)
    P = normalize(P)

    for i in range(max_loop):
        P = inflate(P, inf)
        P = expand(P, exp)
        if stop(P, i):
            break

    cluster = getCluster(P)
    return cluster

def removeDiag(Q):
    n = Q.shape[0]
    for i in range(n):
        Q[i][i] = 1
    return Q

def normalize(Q):
    col_sum = Q.sum(axis = 0)
    Q_normalized = Q / col_sum[np.newaxis, :]
    return Q_normalized

def inflate(Q, inf):
    return normalize(np.power(Q, inf))

def expand(Q, exp):
    return np.linalg.matrix_power(Q, exp)

def stop(Q, i):
    if i % 5 == 4:
        diff = np.max(Q**2 - Q) - np.min(Q**2 - Q)
        if diff == 0:
            return True

    return False

def getCluster(Q):
    cluster = []
    n = Q.shape[0]
    visited = [False] * n
    i = 0;
    while(i < n):
        if visited[i] is True:
            i = i + 1
        else:
            temp, = np.where(Q[i,:] > 0)
            temp = temp.tolist()
            for j in temp:
                visited[j] = True
            cluster.append(temp)
            i = i + 1
    return cluster

if __name__ == "__main__":
    Q = BlockedMatrix(20,3)
    Q[0][2] = 1
    plotGraph(Q, "MCL_Graph")
    print MCL(Q)
