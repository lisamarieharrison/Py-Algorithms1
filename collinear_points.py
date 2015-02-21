import unittest
import numpy as np
import matplotlib.pyplot as plt

class Point(object):

    def __init__(self, x, y):
        # construct the point x, y
        self.x = x
        self.y = y

    def comparator(self, points):
        # Compare points by slope to this point
        slope = []
        for q in points:
            if q.x == self.x and q.y == self.y: # if point is not self, find the slope
                pass
            else:
                dy_dx = (q.y - self.y) / (q.x - self.x)
                slope.append(dy_dx)
        slope_key = sorted(range(len(slope)), key=lambda k: slope[k])
        slope.sort()

        i = 0
        while i < (len(slope) - 1):
            collinear_points = [0]
            while slope[i] == slope[i + 1]:
                collinear_points.append(slope_key[i + 1])
                i += 1
            i += 1
            if len(collinear_points) >= 4:
                return collinear_points
            else:
                return None

    def draw_to(self, point_that):
        # draw a segment from this point to that point
        pass


def draw(point_list):
    # draw all points
    x = []
    y = []
    for point in point_list:
        x.append(point[0])
        y.append(point[1])
    plt.plot(x, y, 'ro')
    plt.axis([0, max(x)*1.2, 0, max(y)*1.2])
    plt.show()

with open('C:/Users/Lisa/Documents/code/collinear/input6.txt') as f:
    next(f)
    point_array = [[float(digit) for digit in line.split()] for line in f]

# create a collection of point objects using the points x and y coordinates
point_collection = []
for point in point_array:
    point_collection.append(Point(x=point[0], y=point[1]))

# plot all points
# draw(point_array)

# find collinear points
p = point_collection[0].comparator(point_collection)
print p

class CollinearPoints(unittest.TestCase):

    def test_point_has_x_and_y(self):
        with open('C:/Users/Lisa/Documents/code/collinear/input2.txt') as f:
            next(f)
            point_array = [[float(digit) for digit in line.split()] for line in f]
        self.assertEqual(2, len(point_array[1]))
