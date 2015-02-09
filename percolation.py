from random import shuffle
import sys
import time

class Percolation():
    def __init__(self, n):
        self.n = n
        self.percolates = False  # does the system percolate?
        self.sz = [1] * (n**2 + 2)  # tree size starts at 1 for all nodes
        self.id = range(0, n**2 + 2)  # 0 = false top and n**2 + 1 == false bottom
        self.is_open = range(1, n**2 + 1)  # which cells are currently open
        self.board = [False] * (n**2 + 2)  # create boolean board of n**2 values + false top and bottom
        # join false top and bottom to first and last rows
        for i in range(1, n + 1):
            self.id[i] = 0
        for i in range(n**2 - n + 1, n**2 + 1):
            self.id[i] = n**2 + 1
        shuffle(self.is_open)

    def root(self, n):
        '''Finds the root of a node

        :param n: Node number
        :return: int'''
        while n != self.id[n]:
            self.id[n] = self.id[self.id[n]]  # path compression
            n = self.id[n]
        return n

    def connected(self, x, y):
        '''Returns true if the two nodes are connected'''
        x_root = self.root(x)
        y_root = self.root(y)
        return x_root == y_root

    def union(self, x, y):
        '''Connects nodes x and y'''
        x_root = self.root(x)
        y_root = self.root(y)
        if y_root == x_root:
            return
        # if roots are not the same, move smaller tree to larger tree
        if self.sz[x_root] < self.sz[y_root]:
            self.id[x_root] = y_root
            self.sz[y_root] += self.sz[x_root]
        else:
            self.id[y_root] = x_root
            self.sz[x_root] += self.sz[y_root]


def run_percolation(n):
    '''
    Runs a single percolation problem
    :param n: Board size
    :return: int giving the percolation threshold
    '''
    run = Percolation(n)

    while not run.percolates:

        # randomly select a cell and open. Only choose from closed cells
        i = run.is_open.pop(0)

        run.board[i] = True

        # connect to neighbours
        neighbours = [i - n, i + n]
        if (i - 1) % n != 0:
            neighbours.append(i - 1)
        if i % n != 0:
            neighbours.append(i + 1)
        for j in neighbours:
            if 0 < j < n**2 + 1:
                if run.board[j]:
                    run.union(i, j)

        # check if percolates
        if run.connected(0, n**2 + 1):
            run.percolates = True

    return float(sum(run.board)) / n**2


def percolation_stats(n, t):
    '''Runs t independent tests of n*n board

    :param n: Board size
    :param t: number of iterations of percolation
    :return: array of threshold estimates'''
    if n < 1 or t < 1:
        sys.exit("Error: Input n and t > 0")
    est = []
    for i in range(1, t + 1):
        est.append(run_percolation(n))
    # print 'Mean:', np.mean(self.est)
    # print 'SD:', np.std(self.est)
    # print '95% confidence interval:', stats.norm.interval(0.05, np.mean(self.est), np.std(self.est))

import cProfile
cProfile.run('percolation_stats(256, 1)')
# start_time = time.clock()
# print percolation_stats(256, 1)
# print 'Time (s):', time.clock() - start_time

