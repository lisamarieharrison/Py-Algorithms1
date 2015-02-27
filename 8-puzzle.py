import numpy as np
import unittest
import math

class Board(object):

    def __init__(self, board, moves_to_reach, previous_node):
        self.board = board
        self.N = np.shape(self.board)[1]
        self.moves_to_reach = moves_to_reach
        self.previous_node = previous_node

    def hamming(self, moves):
        '''number of blocks in wrong position + number of moves to get to node'''
        wrong_position = 0
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.board[i][j] != i*3 + j + 1 and self.board[i][j] > 0:
                    wrong_position += 1
        return wrong_position + moves

    def manhattan(self, moves):
        '''calculates total distance to end + number of moves to get to node'''
        total_distance = 0
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.board[i][j] > 0:
                    target_i = math.floor((self.board[i][j] - 1) / self.N)
                    target_j = math.floor((self.board[i][j] - 1) % self.N)
                    x = math.fabs(i - target_i)
                    y = math.fabs(j - target_j)
                    total_distance += (x + y)
        return total_distance + moves

    def is_goal(self):
        goal_board = np.concatenate([range(1, self.N**2), [0]])
        goal_board = np.reshape(goal_board, (self.N, self.N))
        if np.array_equal(self.board, goal_board):
            return True
        else:
            return False

    def find_empty(self):
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.board[i][j] == 0:
                    empty_i = i
                    empty_j = j
                    break
        return [empty_i, empty_j]

    def find_neighbours(self):
        i = self.board.find_empty()[1]
        j = self.board.find_empty()[2]
        neighbours = []
        if j > 0:
            new = self.board
            new[i][j] = new[i][j - 1]
            new[i][j - 1] = 0
            neighbours.append(new)
        if j < N:
            new = self.board
            new[i][j] = new[i][j + 1]
            new[i][j + 1] = 0
            neighbours.append(new)
        if i < N:
            new = self.board
            new[i][j] = new[i + 1][j]
            new[i + 1][j] = 0
            neighbours.append(new)
        if i > 0:
            new = self.board
            new[i][j] = new[i - 1][j]
            new[i - 1][j] = 0
            neighbours.append(new)

class Solver(object):

    def solver(self):
        pass


with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
    next(f)
    board = [[float(digit) for digit in line.split()] for line in f]

print board

board = Board(board, moves_to_reach=0, previous_node=None)


class EightPuzzle(unittest.TestCase):
    with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
        next(f)
        board = [[float(digit) for digit in line.split()] for line in f]
    board = Board(board, moves_to_reach=0, previous_node=None)

    def test_hamming(self):
        self.assertEqual(7, board.hamming(moves=0))

    def test_manhattan(self):
        self.assertEqual(15, board.manhattan(moves=0))

    def test_is_goal_on_false(self):
        self.assertEqual(False, board.is_goal())

    def test_is_goal_on_true(self):
        goal_board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]], moves_to_reach=0, previous_node=None)
        self.assertTrue(goal_board.is_goal())
