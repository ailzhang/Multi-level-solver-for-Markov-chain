import numpy as np
from scipy.linalg import solve

def gauss(Q, zero, pi, n, dim, lamda):
    pi_next = [0.0, 0.0]
    count = 0
    print "Q=",Q,"zero=",zero,"pi=",pi,"dim=",dim,"lamda=",lamda
    for k in range(1,n):
        for i in range(1,dim+1):
            count = 0
            for j in range(1,i):
                #print "i=",i,"j=",j
                pi_next[i-1] += (-1.0)*(pi_next[j-1]*Q[j-1][i-1])/Q[i-1][i-1]
                '''
                print "i=",i,"j=",j,"upper_half"
                print "Pi[",i,"]",pi[i-1]
                print "Q[",j,"]","[",i,"]=",Q[j-1][i-1]
                print "Q[",i,"]","[",i,"]=",Q[i-1][i-1]
                print "pi_next[",i-1,"]",pi_next[i-1]
                '''
            for j in range(i+1,dim+1):
                print "i=",i,"j=",j
                pi_next[i-1] += (-1.0)*(pi[j-1]*Q[j-1][i-1])/Q[i-1][i-1]
                '''
                print "i=",i,"j=",j,"lower_half"
                print "Pi[",i,"]",pi[i-1]
                print "Q[",j,"]","[",i,"]=",Q[j-1][i-1]
                print "Q[",i,"]","[",i,"]=",Q[i-1][i-1]
                print "pi_next[",i-1,"]",pi_next[i-1]
            print str(k).zfill(4),
            print(pi_next)
            '''
            if(pi_next[i-1]-pi[i-1]<lamda):
                count+=1
            pi = pi_next
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
pi = [1.0, 0.0]#what we are attempting to solve for

n = 46#number of iterations

print "final result!!!"
pi = gauss(Q3, zero, pi, n, 2, l)
print pi

