#####################################################
##      Created on Nov 28, 2015 by Ailing Zhang     ##
#####################################################

import numpy as np

# n is the number of states
# birth is the birth rate
# death is the death rate

def BirthDeath(n,birth,death):
    res = np.zeros((n, n))
    res[0][0] = -birth
    res[n-1][n-1] = -death
    res[0][1] = birth
    res[n-1][n-2] = death
    for i in range(1,n-1):
        res[i][i] = - birth - death
        res[i][i+1] = birth
        res[i][i-1] = death
    return res

'''__main()'''

n = 4
birth = 2
death = 1
print BirthDeath(n, birth, death)
