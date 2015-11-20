import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)#Lower triangle of A
    U = A - L#Upper triangle of A
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))#dot of (inverse of L & dot of (upper triangle of A and x))
        print str(i).zfill(4),
        print(x)
    return x

'''___MAIN___'''
l = 1e-1
A = np.array([[-1.0, 1.0, 0.0, 0.0],\
              [1.0, -1.0-l, 0.0, l], \
              [2*l, 0.0, -1.0-2*l, 1.0],\
              [0.0, 0.0, 1.0, -1.0]])
print A
b = [0.0, 0.0, 0.0, 0.0]#solution to Ax = b
x = [0.25, 0.25, 0.25, 0.25]#what we are attempting to solve for

n = 5#number of iterations

print gauss(A, b, x, n)
print "final result"
print solve(A, b)
