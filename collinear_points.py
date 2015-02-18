import unittest
import plotly.plotly as py
from plotly.graph_objs import *

class Point(object):

    def __init__(self, x, y):
        # construct the point x, y
        self.x = x
        self.y = y

    def comparator(self):
        # Compare points by slope to this point
        pass

    def draw(self):
        # draw this point
        trace = Scatter(
            x=[self.x],
            y=[self.y],
            mode='markers'
        )
        py.plot([trace])

    def draw_to(self, point_that):
        # draw a segment from this point to that point
        pass




with open('C:/Users/Lisa/Documents/code/collinear/input2.txt') as f:
    next(f)
    point_array = [[float(digit) for digit in line.split()] for line in f]

# create a collection of point objects using the points x and y coordinates
point_collection = []
for point in point_array:
    point_collection.append(Point(x=point[0], y=point[1]))

point_collection[1].draw()

class CollinearPoints(unittest.TestCase):

    def test_point_has_x_and_y(self):
        with open('C:/Users/Lisa/Documents/code/collinear/input2.txt') as f:
            next(f)
            point_array = [[float(digit) for digit in line.split()] for line in f]
        self.assertEqual(2, len(point_array[1]))
