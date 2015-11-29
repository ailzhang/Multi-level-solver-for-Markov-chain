import numpy as np
from scipy.linalg import solve
import pdb
from BirthDeath import BirthDeath

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
            return pi_next
        if(stopBylamda == False and count == lamda):
            return pi_next
        pi = pi_next ;

'''___MAIN___'''
if __name__ == "__main__":
    lamda = 1e-7
    n = 6
    birth = 1
    death = 2
    Q = BirthDeath(n, birth, death)
#    Q = np.array([[-1.0, 1.0, 0.0, 0.0],\
#              [1.0, -1.0-l, 0.0, l], \
#              [2*l, 0.0, -1.0-2*l, 1.0],\
#              [0.0, 0.0, 1.0, -1.0]])
    print Q
    print "final result!!!"
    pi = GaussSeidel(Q,n,lamda, True)
    print pi

