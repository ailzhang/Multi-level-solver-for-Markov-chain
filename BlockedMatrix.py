#####################################################
##      Created on Nov 28, 2015 by Ailing Zhang     ##
#####################################################

import numpy as np
from random import *
import pdb
from plotGraph import plotGraph

# n is the number of states
# m is number of blocks

def BlockedMatrix(n,m):
    res = np.zeros((n, n))
    cluster = [[] for x in range(m)]
    for i in range(n):
        r = randint(0, m-1)
	cluster[r].append(i)
    for j in range(m):
	for k in range(len(cluster[j])):
	    local_sum = 0
	    row = cluster[j][k]
	    for l in range (len(cluster[j])):
		col = cluster[j][l]
		if(l!=k):
		    res[row][col]=randint(1, 3)
		    local_sum = local_sum + res[row][col]
	    res[row][row] = -local_sum
    # plotGraph(res, name)
    return res

'''__main()'''
if __name__ == "__main__":
    n = 8
    m = 4
    print BlockedMatrix(n, m)
