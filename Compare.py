from MultiLevel import MultiLevel
from GaussSeidel import GaussSeidel
from BirthDeath import BirthDeath
import numpy as np
import math
import time
import sys

#    n = 100
start = time.time()
n = int(sys.argv[1])
birth = 1
death = 1
Q = BirthDeath(n, birth, death) #generate transition matrix
P = np.transpose(Q)
grid = 4
#    pdb.set_trace()
level = int(math.log(n, 4))
print level
iterations = 0;
pi, iterations = MultiLevel(P, level, iterations, grid)
lamda = 1e-7
piG, iterationsG = GaussSeidel(Q, n, lamda, True)
print "MultiLevel:", pi
print "GaussSeidel:", piG
print "Difference: ", np.linalg.norm(pi-piG)
end = time.time()
print "Number of Iterations: ", iterations
print "Number of States: ", n
print "Time Elapsed: ", end-start, " seconds"
