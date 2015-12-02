#####################################################
##      Created on Nov 28, 2015 by Ailing Zhang    ##
#####################################################
import numpy as np
from BirthDeath import BirthDeath
from GaussSeidel import GaussSeidel
from numpy import linalg
from GraphConnectedComponents import GraphPartitionByConnectedComponent
from Graph_MCL import GraphPartitionByMCL
import math
import pdb
import time
import sys

def MultiLevel(P, grid = 4, strategy = 1):
    n = P.shape[0];
    count = 0;
    if  n <= 2 * grid:
#        return linalg.solve(P, np.zeros((n,1)))

        return GaussSeidel(np.transpose(P), n, 1e-7, True)
    else:
#        p_tilde = GaussSeidel(np.transpose(P), n, 3, False)
#        cluster = Partition(P)
#        P_next, p_tilde_next = Coarse(P, p_tilde, cluster)
#        p_bar_next = MultiLevel(P_next, level-1)
        p_tilde, subcount = GaussSeidel(np.transpose(P), n, 20, False)
        count += subcount

        if strategy == 1:
            cluster = Partition(P, grid)
        # elif strategy == 2:
        #     cluster = GraphPartitionByConnectedComponent(P)
        elif strategy == 3:
            cluster = GraphPartitionByMCL(np.transpose(P))
        else:
            print "Invalid strategy!"
        strategy = 1
        start = time.time()
        P_next, p_tilde_next = Coarse(P, p_tilde, cluster);
        end = time.time()
        print "Coarse Time:", end-start
        for i in range(P_next.shape[0]):
            if P_next[i][i] == 0:
                return GaussSeidel(np.transpose(P), n, 1e-7, True)
        p_bar_next, subcount = MultiLevel(P_next, grid, strategy)
        p_star_next = np.divide(p_bar_next, p_tilde_next)
        p_star = I(p_star_next, n, cluster)
        p_bar = C(p_tilde, p_star)
        return (p_bar / np.sum(p_bar), count+subcount)

def Partition(P, grid):
    n = P.shape[0];#return demension of P
    originalset = range(n)
    cluster = [originalset[i:i+grid] for i in range(0, (n / grid - 1) * grid,grid)]
    cluster.append(range((n/grid-1)*grid, n))#[[0,1],[2,3],[4,5]]
    return cluster

#equation 12
def Coarse(P, p_tilde, cluster):
    n = len(cluster)
    P_next = np.zeros((n,n))
    p_tilde_next = np.zeros((n,1))
    for i in range(n):
        for j in cluster[i]:
            p_tilde_next[i] += p_tilde[j]

    for i in range(n):
        for j in range(n):
            sum = 0
            for k in cluster[i]:
                sum_i = 0
                for l in cluster[j]:
                    sum_i += P[l][k]
                sum += sum_i * p_tilde[k]
            P_next[j][i] = sum / p_tilde_next[i]
#    print "P_next:", P_next
    print "P_next length:", len(P_next), "p_tilde_next length:", len(p_tilde_next)
    return (P_next, p_tilde_next)

def I(p_star_next, n, cluster):
    p_star = np.zeros((n,1))
    for i in range(len(cluster)):
        for j in cluster[i]:
            p_star[j] = p_star_next[i]
    return p_star

def C(p_tilde, p_star):
    p_bar = np.multiply(p_tilde, p_star)
    return p_bar

if __name__ == "__main__":
#    n = 100
    start = time.time()
    n = int(sys.argv[1])
    birth = 1
    death = 2
    grid = 4
    Q = BirthDeath(n, birth, death) #generate transition matrix
    P = np.transpose(Q)
#    pdb.set_trace()
    level = int(math.log(n, grid))
    print level
    iterations = 0;
    pi, iterations = MultiLevel(P, grid, 3)
    #print pi
    end = time.time()
    print "Number of Iterations: ", iterations
    print "Number of States: ", n
    print "Time Elapsed: ", end-start, " seconds"
