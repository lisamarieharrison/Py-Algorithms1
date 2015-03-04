import unittest
import matplotlib.pyplot as plt


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


class PointSet(object):

    def __init__(self, points):
        point_set = []
        for point in points:
            point_set.append(Point2D(point[0], point[1]))
        self.point_set = point_set

    def is_empty(self):
        '''checks if the set is empty and returns boolean'''
        if len(self.point_set) == 0:
            return True
        else:
            return False

    def size(self):
        '''returns the number of points in the set'''
        return len(self.point_set)

    def draw(self):
        '''draw all points in the point list'''
        x = []
        y = []
        for p in self.point_set:
            x.append(p.x)
            y.append(p.y)
        plt.plot(x, y, 'ro')
        plt.axis([0, 1, 0, 1])
        plt.show()

    def insert(self, new_point):
        '''inserts a points into the set if it is not already present'''
        for point in self.point_set:
            if new_point.x == point.x and new_point.y == point.y:
                return False
        self.point_set.append(new_point)
        return True



with open('C:/Users/Lisa/Documents/code/kdtree/input10K.txt') as f:
    point_array = [[float(digit) for digit in line.split()] for line in f]

# turn points into point objects
point_obj = PointSet(point_array)

# draw all points
#point_obj.draw()


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

    def test_is_empty_on_true(self):
        point_array = []
        point_obj = PointSet(point_array)
        self.assertTrue(point_obj.is_empty())

    def test_is_empty_on_false(self):
        point_array = [[1, 2], [3, 4]]
        point_obj = PointSet(point_array)
        self.assertEqual(False, point_obj.is_empty())

    def test_size(self):
        point_array = [[1, 2], [3, 4]]
        point_obj = PointSet(point_array)
        self.assertEqual(2, point_obj.size())

    def test_insert_on_unique(self):
        point_array = [[1, 2], [3, 4]]
        point_obj = PointSet(point_array)
        new_point = Point2D(1, 6)
        added = point_obj.insert(new_point)
        self.assertTrue(added)
        self.assertEqual(3, point_obj.size())

    def test_insert_on_duplicate(self):
        point_array = [[1, 2], [3, 4]]
        point_obj = PointSet(point_array)
        new_point = Point2D(1, 2)
        added = point_obj.insert(new_point)
        self.assertEqual(False, added)
        self.assertEqual(2, point_obj.size())