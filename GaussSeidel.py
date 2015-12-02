import sys
import numpy as np
from scipy.linalg import solve
import pdb
from BirthDeath import BirthDeath
import time

# GaussSeidel is a function that compute steady-state solution using GaussSeidel
# method. We can can stop the iteration by lamda. And lamda has two meanings.
# When stopBylamda is set true, iterations will stop when ||pi - pi_next|| < lamda.
# When it's set false, GaussSeidel will stop after running lamda iterations.   

def GaussSeidel(Q, n, lamda, stopBylamda):
    pi = np.ones((n,1))
    count = 0
    while True:
        count = count + 1
        pi_next = np.zeros((n,1))
        for i in range(0,n):
            for j in range(0,i):
                pi_next[i] += (-1.0)*(pi_next[j]*Q[j][i])/Q[i][i]
            for j in range(i+1,n):
                pi_next[i] += (-1.0)*(pi[j]*Q[j][i])/Q[i][i]
        pi_next = pi_next / np.sum(pi_next);
        if(stopBylamda == True and np.linalg.norm(pi_next - pi) < lamda):
            return (pi_next, count)
        if(stopBylamda == False and count == lamda):
            return (pi_next, count)
        pi = pi_next ;


'''___MAIN___'''
if __name__ == "__main__":
    start = time.time()
    lamda = 1e-7
#    n = 100
    n = int(sys.argv[1])
    birth = 1
    death = 2
    Q = BirthDeath(n, birth, death)
    iterations = 0;
    pi, iterations = GaussSeidel(Q,n,lamda, True)
    end = time.time()
    print "Number of Iterations: ", iterations
    print "Number of States: ", n
    print "Time Elapsed: ", end-start, " seconds"
