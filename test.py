import numpy as np
from scipy import stats
import math
from random import shuffle
import sys
import time

start_time = time.clock()
class Percolation():

    def __init__(self, N):
        self.N = N
        self.percolates = False #does the system percolate?
        self.sz = [1]*(N**2 + 2) #tree size starts at 1 for all nodes
        self.id = np.reshape(range(0, N**2 + 2), N, N) #0 = false top and N**2 + 1 == false bottom
        self.is_open = range(1, N**2 + 1) #which cells are currently open
        shuffle(self.is_open)

    def findRow(self, x):
        return math.floor(x / self.N)

    def findCol(self, x, r):
         return x - r * self.N

    def percolation(self, N):
        '''
        Creates an N*N board
        :param N: Dimension of square board
        :return: board
        '''

        self.board = [False] * (N**2 + 2) #create boolean board of N**2 values + false top and bottom

        #join false top and bottom to first and last rows
        self.id[1:(N + 1)] = [0]*N
        self.id[(N**2 - N + 1): (N**2 + 1)] = [N**2 + 1]*N

    def root(self, n):
        '''
        Finds the root of a node
        :param n: Node number
        :return: int
        '''
        while n != self.id[n]:
            self.id[n] = self.id[self.id[n]] #path compression
            n = self.id[n]
        return n

    def connected(self, x, y):
        '''
        :param x: First node
        :param y: Second node
        :return: bool
        '''
        x_root = self.root(x)
        y_root = self.root(y)
        return x_root == y_root

    def union(self, x, y):
        '''
        :param x: First node
        :param y: Second node
        :return: nothing
        '''
        x_root = self.root(x)
        y_root = self.root(y)
        if y_root == x_root:
            return
        #if roots are not the same, move smaller tree to larger tree
        if self.sz[x_root] < self.sz[y_root]:
            self.id[x_root] = y_root
            self.sz[y_root] += self.sz[x_root]
        else:
            self.id[y_root] = x_root
            self.sz[x_root] += self.sz[y_root]


def runPercolation(N):
    '''
    Runs a single percolation problem
    :param N: Board size
    :return: int giving the percolation threshold
    '''
    run = Percolation(N)
    run.percolation(N)

    while run.percolates == False:

        #randomly select a cell and open. Only choose from closed cells
        i = run.is_open[0]
        run.is_open.pop(0)
        run.board[i] = True

        #connect to neighbours
        neighb = [i - N, i + N]
        if (i - 1) % N != 0:
            neighb.append(i - 1)
        if i % N != 0:
            neighb.append(i + 1)
        for j in neighb:
            if 0 < j < N**2 + 1:
                if run.board[j]:
                    run.union(i, j)

        #check if percolates
        if run.connected(0, N**2 + 1):
            run.percolates = True

    return float(sum(run.board)) / N**2

class PercolationStats():
    '''
    Percolation Statistics for T independent tests of N*N board
    '''

    def percolationStats(self, N, T):
        '''
        Runs T independent tests of N*N board
        :param N: Board size
        :param T: Number of iterations of percolation
        :return: array of threshold estimates
        '''
        if N < 1 or T < 1:
            sys.exit("Error: Input N and T > 0")
        self.est = []
        for i in range(1, T + 1):
            self.est.append(runPercolation(N))
        # print 'Mean:', np.mean(self.est)
        # print 'SD:', np.std(self.est)
        # print '95% confidence interval:', stats.norm.interval(0.05, np.mean(self.est), np.std(self.est))

test = PercolationStats()
print test.percolationStats(256, 1)
print 'Time (s):', time.clock() - start_time

