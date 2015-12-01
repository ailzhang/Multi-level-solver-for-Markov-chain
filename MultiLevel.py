#####################################################
##      Created on Nov 28, 2015 by Ailing Zhang    ##
#####################################################
import numpy as np
from BirthDeath import BirthDeath
from GaussSeidel import GaussSeidel
from numpy import linalg
import pdb
import time 
import sys

def MultiLevel(P, level, count):
    n = P.shape[0];
    subcount = 0;
    if level == 0:
#        return linalg.solve(P, np.zeros((n,1)))
        return GaussSeidel(np.transpose(P), n, 1e-7, True)
    else:
#        p_tilde = GaussSeidel(np.transpose(P), n, 3, False)
#        cluster = Partition(P)
#        P_next, p_tilde_next = Coarse(P, p_tilde, cluster)
#        p_bar_next = MultiLevel(P_next, level-1)
        p_tilde, subcount = GaussSeidel(np.transpose(P), n, 3, False)
        count += subcount
        cluster = Partition(P);
        P_next, p_tilde_next = Coarse(P, p_tilde, cluster);
        p_bar_next, count = MultiLevel(P_next, level-1, count)
        p_star_next = np.divide(p_bar_next, p_tilde_next)
        p_star = I(p_star_next, n, cluster)
        p_bar = C(p_tilde, p_star)
        return (p_bar / np.sum(p_bar), count)

def Partition(P):
    n = P.shape[0];#return demension of P
    grid = 2
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
    Q = BirthDeath(n, birth, death) #generate transition matrix
    P = np.transpose(Q)
    #pdb.set_trace()
    level = 1
    iterations = 0;
    pi, iterations = MultiLevel(P, level, iterations)
    #print pi
    end = time.time()
    print "Number of Iterations: ", iterations
    print "Number of States: ", n
    print "Time Elapsed: ", end-start, " seconds"
