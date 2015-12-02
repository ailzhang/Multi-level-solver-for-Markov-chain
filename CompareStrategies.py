#####################################################
##      Created on Dec 1, 2015 by Ailing Zhang     ##
#####################################################
from MultiLevel import MultiLevel
from BlockedMatrix import BlockedMatrix
import time
import sys
import numpy as np
from plotGraph import plotGraph
from GaussSeidel import GaussSeidel


n = int(sys.argv[1])
m = int(sys.argv[2])
Q = BlockedMatrix(n, m)
plotGraph(Q, "blockmatrix")
P = np.transpose(Q)
#    pdb.set_trace()
start = time.time()
pi, iterations = MultiLevel(P, strategy = 3)
end = time.time()
print "Number of Iterations: ", iterations
print "Number of States: ", n
print "Time Elapsed: ", end-start, " seconds"
start = time.time()
pi_1, iterations_1 = MultiLevel(P, strategy = 1)
#print pi
end = time.time()
print "Number of Iterations: ", iterations_1
print "Number of States: ", n
print "Time Elapsed: ", end-start, " seconds"

pi_G, iterations_G = GaussSeidel(P, n, 1e-7, True)
print np.linalg.norm(pi-pi_G)
print np.linalg.norm(pi_1-pi_G)
