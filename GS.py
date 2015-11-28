import numpy as np
from scipy.linalg import solve

import pdb

def gauss(Q, zero, pi, n, dim, lamda):
    
    count = 0
    pdb.set_trace()
    for k in range(0,n):
        pi_next = [0.0, 0.0,0.0, 0.0]
        for i in range(0,dim):
            count = 0
            for j in range(0,i):
                pi_next[i] += (-1.0)*(pi_next[j]*Q[j][i])/Q[i][i]
            for j in range(i+1,dim):
                print "i=",i,"j=",j
                pi_next[i] += (-1.0)*(pi[j]*Q[j][i])/Q[i][i]
        print str(k).zfill(4),
        print(pi_next)
            
        if(abs(pi_next[i]-pi[i]) < lamda):
            count+=1
        pi_next = pi_next / np.sum(pi_next);
        pi = pi_next ;
        if(count>=dim):
            print "BREAK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            break

    return pi/np.sum(pi)

'''___MAIN___'''
l = 1e-1
Q = np.array([[-1.0, 1.0, 0.0, 0.0],\
              [1.0, -1.0-l, 0.0, l], \
              [2*l, 0.0, -1.0-2*l, 1.0],\
              [0.0, 0.0, 1.0, -1.0]])
'''
Q2 = np.array([[-2.0, 2.0, 0.0],\
               [0.0, -1.0, 1.0], \
               [1.5, 1.5, -3.0]])
'''

Q3 = np.array([[-1.0, 1.0],\
              [1.0, -1.0]])
#print Q
zero = [0.0, 0.0, 0.0, 0.0]#solution to Ax = b
pi = [1.0,1.0,1.0,1.0]#what we are attempting to solve for

n = 46#number of iterations

print "final result!!!"
pi = gauss(Q, zero, pi, n, 4, l)
print pi

