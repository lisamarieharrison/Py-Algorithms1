import numpy as np
import unittest

class Board(object):

    def __init__(self, board):
        self.board = board
        self.N = np.shape(self.board)[1]

    def hamming(self):
        wrong_position = 0
        for i in range(0, self.N):
            for j in range(0, self.N):
                if self.board[i][j] != i*3 + j + 1 and self.board[i][j] > 0:
                    wrong_position += 1
        return wrong_position


with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
    next(f)
    board = [[float(digit) for digit in line.split()] for line in f]

print board

board = Board(board)


class EightPuzzle(unittest.TestCase):
    with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
        next(f)
        board = [[float(digit) for digit in line.split()] for line in f]
    board = Board(board)

    def test_hamming(self):
        self.assertEqual(7, board.hamming())
