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

# CompareStragies is used to compare the performance of basic grouping strategy
# and the MCL clustering strategy.

n = int(sys.argv[1])
m = int(sys.argv[2])
Q = BlockedMatrix(n, m)
plotGraph(Q, "blockmatrix")
P = np.transpose(Q)
# MCL
start = time.time()
pi, iterations = MultiLevel(P, strategy = 3)
end = time.time()
print "Number of Iterations: ", iterations
print "Number of States: ", n
print "Time Elapsed: ", end-start, " seconds"
# Basic strategy
start = time.time()
pi_1, iterations_1 = MultiLevel(P, strategy = 1)
end = time.time()
print "Number of Iterations: ", iterations_1
print "Number of States: ", n
print "Time Elapsed: ", end-start, " seconds"

# Use GaussSeidel as a baseline of steady-state solution
pi_G, iterations_G = GaussSeidel(P, n, 1e-7, True)
print np.linalg.norm(pi-pi_G)
print np.linalg.norm(pi_1-pi_G)
