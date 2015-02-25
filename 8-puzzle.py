import numpy as np
import unittest
import math

class Board(object):

    def __init__(self, board):
        self.board = board
        self.N = np.shape(self.board)[1]

    def hamming(self, moves):
        wrong_position = 0
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.board[i][j] != i*3 + j + 1 and self.board[i][j] > 0:
                    wrong_position += 1
        return wrong_position + moves

    def manhattan(self, moves):
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


with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
    next(f)
    board = [[float(digit) for digit in line.split()] for line in f]

print board

board = Board(board)

print board.manhattan(0)

class EightPuzzle(unittest.TestCase):
    with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
        next(f)
        board = [[float(digit) for digit in line.split()] for line in f]
    board = Board(board)

    def test_hamming(self):
        self.assertEqual(7, board.hamming(moves=0))

    def test_manhattan(self):
        self.assertEqual(15, board.manhattan(moves=0))
