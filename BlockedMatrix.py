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
    print cluster
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
    print res
    plotGraph(res, "orignal")
    for c1 in range(m):
        for c2 in range(m):
            if c1 != c2 and len(cluster[c1])>0 and len(cluster[c2]) > 0:
                row = cluster[c1][randint(0, len(cluster[c1])-1)]
                col = cluster[c2][randint(0, len(cluster[c2])-1)]
                res[row][col] = 1
                res[row][row] = res[row][row] - res[row][col]
                print (row, col)
    return res

'''__main()'''
if __name__ == "__main__":
    n = 100
    m = 4
    Q = BlockedMatrix(n, m)
    plotGraph(Q, "general")
