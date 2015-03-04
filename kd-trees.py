import unittest


class Point2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point2):
        '''calculates the Euclidean distance between two points'''
        x_dist = self.x - point2.x
        y_dist = self.y - point2.y
        euc_dist = (x_dist**2 + y_dist**2)**0.5
        return euc_dist

    def distance_squared_to(self, point2):
        '''calculates the squared Euclidean distance between two points'''
        x_dist = self.x - point2.x
        y_dist = self.y - point2.y
        sqr_dist = x_dist**2 + y_dist**2
        return sqr_dist

    def equals(self, point2):
        '''are two points equal?'''
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False


with open('C:/Users/Lisa/Documents/code/kdtree/input10K.txt') as f:
    point_array = [[float(digit) for digit in line.split()] for line in f]

print len(point_array)

#
# for i in p:
#     min_point.append([find_first(point_collection, i)])
#     max_point.append([find_last(point_collection, i)])
# draw_to(min_point, max_point, point_array)


class CollinearPoints(unittest.TestCase):

    def test_distance_to(self):
        point1 = Point2D(x=0, y=0)
        point2 = Point2D(x=0.5, y=0.5)
        self.assertEqual(0.5**0.5, point1.distance_to(point2))

    def test_distance_squared_to(self):
        point1 = Point2D(x=0, y=0)
        point2 = Point2D(x=0.5, y=0.5)
        self.assertEqual(0.5, point2.distance_squared_to(point1))

    def test_equals_on_true(self):
        point1 = Point2D(x=0, y=0)
        point2 = Point2D(x=0, y=0)
        self.assertTrue(point1.equals(point2))

    def test_equals_on_false(self):
        point1 = Point2D(x=0, y=0)
        point2 = Point2D(x=0, y=0.5)
        self.assertEqual(False, point2.equals(point1))