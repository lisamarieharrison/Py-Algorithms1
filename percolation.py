import numpy as np
import random

N = 20
percolates = False
open = 0
id = range(0, N**2 + 2) #0 = false top and N**2 + 1 == false bottom
sz = np.ones((N**2 + 2)) #tree size starts at 1
is_open = range(1, N**2 + 1)

def root(n):
    """Finds the root of a node
    :rtype: int
    """
    while n != id[n]:
        n = id[n]
    return n

def union(x, y):
    """Creates a union between two nodes
    :rtype: nothing
    """
    x_root = root(x)
    y_root = root(y)
    if y_root != x_root:
        id[y_root] = x
        sz[x] += sz[y]

def connected(x, y):
    """Checks whether two nodes are connected
    :rtype: bool
    """
    x_root = root(x)
    y_root = root(y)
    return x_root == y_root


#join top and bottom to top and bottom rows
for i in range(1, N):
    id[i] = 0
for i in range(N**2 - N + 1, N**2 + 1):
    id[i] = N**2 + 1

#creat board. site is blocked if cell == 0
board = np.zeros((N**2 + 2))


while percolates == False:

    #randomly select a cell and open
    if is_open:
        i = random.choice(is_open)
        is_open.remove(i)
    board[i] = 1
    open += 1

    #connect to neighbours
    neighb = [i - N, i + N]
    if (i - 1) % N != 0:
        neighb.append(i - 1)
    if i % N != 0:
        neighb.append(i + 1)
    for j in neighb:
        if j in range(1, N**2 + 1):
            if board[j] == 1:
                union(i, j)
    #check if percolates
    if connected(0, N**2 + 1):
        percolates = True

print float(open) / N**2

'''
#optionally print out the board
for i in range(1, N**2 - (N - 2), N):
    print board[range(i, i + N)]
'''
