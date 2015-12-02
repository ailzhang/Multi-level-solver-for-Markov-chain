#####################################################
##      Created on Dec 1, 2015 by Ailing Zhang     ##
#####################################################
from MultiLevel import MultiLevel
from BlockedMatrix import BlockedMatrix

start = time.time()
n = int(sys.argv[1])
m = int(sys.argv[2])
Q = BlockedMatrix(n, m)
P = np.transpose(Q)
#    pdb.set_trace()
level = int(math.log(n, grid))
print level
iterations = 0;
pi, iterations = MultiLevel(P, level, iterations, grid, )
#print pi
end = time.time()
print "Number of Iterations: ", iterations
print "Number of States: ", n
print "Time Elapsed: ", end-start, " seconds"
