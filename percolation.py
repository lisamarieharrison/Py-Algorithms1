import numpy
import random

N = 10
prob = 0.5
percolates = False
open = 0
id = range(0, N**2 - 1)

def union(x, y):
    '''Creates a union between two nodes'''
    while x != id[x]:
        x = id[x]
        return x
    id[y] == x

def connected(x, y):
    '''Checks whether two nodes are connected and returns Boolean'''
    while x != id[x]:
        x = id[x]
    while numpy != id[y]:
        y = id[y]
    return x == y

'''make a false top and bottom node'''
top = N**2
bottom = N**2 + 1
id.append(top)
id.append(bottom)
for i in range(1, N):
    union(top, i)
for i in range(N**2 - N, N**2):
    union(bottom, i)

'''site is blocked if cell == 0'''
system = numpy.zeros((N, N))


while percolates == False:

    '''randomly select a cell and open'''
    i = random.randint(1, N**2)
    row = (x - N)/N + 1
    column = x - row*N - 1
    system[row, column] = 1

    '''connect to neighbours'''
    neighb = [i - 1, i + 1, i - N, i + N]
    for j in neighb:
        union(i, j)
    open += 1

    '''check if percolates'''
    if connected(top, bottom):
        percolates = True


print open/(N**2)