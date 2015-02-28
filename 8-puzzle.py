import numpy as np
import unittest
import math
from Queue import PriorityQueue


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
        return [empty_i, empty_j]

    def clone_board(self):
        new = [[0 for x in range(self.N)] for x in range(self.N)]
        for i in range(0, self.N):
            for j in range(0, self.N):
                new[i][j] = int(self.board[i][j])
        return new

    def find_neighbours(self):
        i = self.find_empty()[0]
        j = self.find_empty()[1]
        neighbours = []
        if j > 0:
            new = self.clone_board()
            new[i][j] = new[i][j - 1]
            new[i][j - 1] = 0
            neighbours.append(new)
        if j < self.N - 1:
            new = self.clone_board()
            new[i][j] = new[i][j + 1]
            new[i][j + 1] = 0
            neighbours.append(new)
        if i < self.N - 1:
            new = self.clone_board()
            new[i][j] = new[i + 1][j]
            new[i + 1][j] = 0
            neighbours.append(new)
        if i > 0:
            new = self.clone_board()
            new[i][j] = new[i - 1][j]
            new[i - 1][j] = 0
            neighbours.append(new)
        return neighbours

    def solver(self):

        queue = PriorityQueue()
        current = self
        queue.put((current.manhattan(moves=0), current))

        while not current.is_goal():

            # remove minimum priority and find neighbours
            current = queue.get()[1]
            neighbours = current.find_neighbours()
            # add neighbours to priority queue
            for i in range(0, len(neighbours)):
                moves = current.moves_to_reach + 1
                if current.previous_node is None:
                    neighbours[i] = Board(neighbours[i], moves_to_reach=moves, previous_node=current)
                    queue.put((neighbours[i].manhattan(moves=moves), neighbours[i]))
                else:
                    if neighbours[i] != current.previous_node.board:
                        neighbours[i] = Board(neighbours[i], moves_to_reach=moves, previous_node=current)
                        queue.put((neighbours[i].manhattan(moves=moves), neighbours[i]))
        return current

    def solution(self):
        last_node = self
        node_trace = []
        while last_node.previous_node is not None:
            node_trace = [last_node.board] + node_trace
            last_node = last_node.previous_node
        return node_trace


with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
    next(f)
    board = [[float(digit) for digit in line.split()] for line in f]

board = Board(board, moves_to_reach=0, previous_node=None)

solve = board.solver()
print solve.moves_to_reach

solution = solve.solution()
for row in solution:
    for r in row:
        print r
    print

class EightPuzzle(unittest.TestCase):

    def setUp(self):
        with open('C:/Users/Lisa/Documents/code/8puzzle/puzzle25.txt') as f:
            next(f)
            self.board = [[float(digit) for digit in line.split()] for line in f]
        self.board = Board(self.board, moves_to_reach=0, previous_node=None)

    def test_hamming(self):
        self.assertEqual(7, self.board.hamming(moves=0))

    def test_manhattan(self):
        self.assertEqual(15, self.board.manhattan(moves=0))

    def test_is_goal_on_false(self):
        self.assertEqual(False, self.board.is_goal())

    def test_is_goal_on_true(self):
        goal_board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]], moves_to_reach=0, previous_node=None)
        self.assertTrue(goal_board.is_goal())

    def test_find_neighbours(self):
        goal_neighbours = [[[2.0, 8.0, 5.0], [3.0, 6.0, 1.0], [0, 7.0, 4.0]], [[2.0, 8.0, 5.0], [3.0, 6.0, 1.0], [7.0, 4.0, 0]], [[2.0, 8.0, 5.0], [3.0, 0, 1.0], [7.0, 6.0, 4.0]]]
        self.assertEqual(goal_neighbours, self.board.find_neighbours())

    def test_queue_put(self):
        queue = PriorityQueue()
        queue.put((self.board.manhattan(moves=0), self.board))
        current = queue.get()[1]
        neighbours = current.find_neighbours()
        # add neighbours to priority queue
        for i in range(0, len(neighbours)):
            moves = current.moves_to_reach + 1
            neighbours[i] = Board(neighbours[i], moves_to_reach=moves, previous_node=current)
            queue.put((neighbours[i].manhattan(moves=moves), neighbours[i]))
        self.assertEqual(3, queue.qsize())

    def test_solver_correct_number_of_moves(self):
        moves = self.board.solver().moves_to_reach
        self.assertEqual(25, moves)
