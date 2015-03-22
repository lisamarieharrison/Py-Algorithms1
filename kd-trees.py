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

RED = True
BLACK = False


def is_red(node):
    if node is None:
        return False # null links are black
    if node.colour is BLACK:
        return False
    else:
        node.colour = RED
        return True

class Node(object):

    def __init__(self, key, val, colour=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.colour = colour

    def rotate_left(self):
        x = self.right
        self.right = x.left
        x.left = self
        x.colour = self.colour
        self.colour = RED
        return x

    def rotate_right(self):
        x = self.left
        self.left = x.right
        x.right = self
        x.colour = self.colour
        self.colour = RED
        return x

    def flip_colours(self):
        self.colour = RED
        self.left.colour = BLACK
        self.right.colour = BLACK

    def compare_to(self, h):
        return self.key - h.key


def put(h, key, val):
    if h is None:
        return Node(key=key, val=val, colour=RED)
    else:
        cmp = key - h.key
        if cmp < 0:
            h.left = put(h=h.left, key=key, val=val)
        elif cmp > 0:
            h.right = put(h=h.right, key=key, val=val)
        elif cmp == 0:
            h.val = val

    if is_red(h.right) and not is_red(h.left):
        h = h.rotate_left()
    if is_red(h.left) and is_red(h.left.left):
        h = h.rotate_right()
    if is_red(h.left) and is_red(h.right):
        h.flip_colours()

    return h


class KdTree(object):

    def __init__(self, root=None):
        self.root = root
        self.current = self.root
        self.level = 1
        self.size = 0

    def insert(self, node):

        if self.root is None:
            self.root = node
            self.root.depth = 1
            self.current = self.root
            self.size += 1
            return True

        if self.current.key == node.key:
            return False

        if self.level % 2 == 0:
            if node.key[1] < self.current.key[1]:
                if self.current.left is None:
                    self.current.left = node
                    self.level = 1
                    self.size += 1
                    self.current.left.depth = self.current.depth + 1
                    self.current = self.root
                    return True
                else:
                    self.current = self.current.left
                    self.level += 1
                    self.insert(node)
            else:
                if self.current.right is None:
                    self.current.right = node
                    self.level = 1
                    self.size += 1
                    self.current.right.depth = self.current.depth + 1
                    self.current = self.root
                    return True
                else:
                    self.current = self.current.right
                    self.level += 1
                    self.insert(node)
        else:
            if node.key[0] < self.current.key[0]:
                if self.current.left is None:
                    self.current.left = node
                    self.level = 1
                    self.size += 1
                    self.current.left.depth = self.current.depth + 1
                    self.current = self.root
                    return True
                else:
                    self.current = self.current.left
                    self.level += 1
                    self.insert(node)
            else:
                if self.current.right is None:
                    self.current.right = node
                    self.level = 1
                    self.size += 1
                    self.current.right.depth = self.current.depth + 1
                    self.current = self.root
                    return True
                else:
                    self.current = self.current.right
                    self.level += 1
                    self.insert(node)

        return True

class KdNode(object):

    def __init__(self, point, value, left=None, right=None, depth=None):
        self.left = left
        self.right = right
        self.key = point
        self.value = value
        self.depth = depth


class PointSet(object):

    def __init__(self, points):
        self.points = points
        self.point_set = KdTree()
        for point in points:
            self.point_set.insert(KdNode(point, Point2D(point[0], point[1])))

    def is_empty(self):
        '''checks if the set is empty and returns boolean'''
        if self.point_set.root is None:
            return True
        else:
            return False

    def size(self):
        '''returns the number of points in the set'''
        return self.point_set.size

    def draw(self):
        '''draw all points in the point list'''
        x = []
        y = []
        current = [self.point_set.root]
        while len(current) >0:
            node = current[0]
            x.append(node.key[0])
            y.append(node.key[1])
            if node.left is not None:
                current.append(node.left)
            if node.right is not None:
                current.append(node.right)
            current.pop(0)
        plt.plot(x, y, 'ro')
        plt.axis([0, 1, 0, 1])
        plt.show()

    def insert(self, new_point):
        '''inserts a points into the set if it is not already present'''
        self.point_set.insert(KdNode(new_point, Point2D(new_point[0], new_point[1])))

    def range(self, rect):
        '''return all points within the rectangle'''
        current = [self.point_set.root]
        points_in_rect = []
        while len(current) > 0:
            node = current[0]
            current.pop(0)
            if rect.contains(node.value):
                points_in_rect.append(node.value)
            if node.depth % 2 == 0:
                rectangle1 = RectHV(0, 1, 0, node.key[1])
                rectangle2 = RectHV(0, 1, node.key[1], 1)
            else:
                rectangle1 = RectHV(0, node.key[0], 0, 1)
                rectangle2 = RectHV(node.key[0], 1, 0, 1)
            if rect.intersects(rectangle1):
                if node.left is not None:
                    current.append(node.left)
            if rect.intersects(rectangle2):
                if node.right is not None:
                    current.append(node.right)
        return points_in_rect



class RectHV(object):

    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def contains(self, p):
        '''does this rectangle contain point p?'''
        return self.xmin <= p.x <= self.xmax and self.ymin <= p.y <= self.ymax

    def intersects(self, rect):
        '''does this rectangle intersect that rectangle?'''
        return self.xmax >= rect.xmin and self.ymax >= rect.ymin and rect.xmax >= self.xmin and rect.ymax >= self.ymin
#
# with open('C:/Users/Lisa/Documents/code/kdtree/input10K.txt') as f:
#     point_array = [[float(digit) for digit in line.split()] for line in f]
#
# # turn points into point objects
# point_obj = PointSet(point_array)

# draw all points
#point_obj.draw()


class KdTrees(unittest.TestCase):

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
        added = point_obj.point_set.insert(KdNode([new_point.x, new_point.y], new_point))
        self.assertTrue(added)
        self.assertEqual(3, point_obj.size())

    def test_insert_on_duplicate(self):
        point_array = [[1, 2], [3, 4]]
        point_obj = PointSet(point_array)
        new_point = Point2D(3, 4)
        added = point_obj.point_set.insert(KdNode([new_point.x, new_point.y], new_point))
        self.assertTrue(added)
        self.assertEqual(2, point_obj.size())

    def test_rbt_insert_key(self):
        start = put(h=None, key=1, val="1")
        second = put(h=start, key=2, val="2")
        third = put(h=second, key=1.5, val="3")
        self.assertEqual([1.5, 1, 2], [third.key, third.left.key, third.right.key])

    def test_rbt_insert_colour(self):
        start = put(h=None, key=1, val="1")
        second = put(h=start, key=2, val="2")
        third = put(h=second, key=1.5, val="3")
        self.assertEqual([True, False, False], [third.colour, third.left.colour, third.right.colour])

    def test_kd_node(self):
        point_array = [[1, 2], [3, 4]]
        node = KdNode(point_array[0], Point2D(point_array[0][0], point_array[0][1]))
        self.assertEqual([1, 2], node.key)

    def test_kd_tree_root(self):
        point_array = [[10, 10], [5, 5], [15, 2], [8, 3]]
        tree = KdTree()
        for point in point_array:
            tree.insert(KdNode(point, Point2D(point[0], point[1])))
        self.assertEqual([10, 10], tree.root.key)

    def test_RectHV_contains_on_True(self):
        rect = RectHV(0, 5, 3, 6)
        p = Point2D(1, 4)
        self.assertTrue(rect.contains(p))

    def test_RectHV_contains_on_False(self):
        rect = RectHV(0, 5, 3, 6)
        p = Point2D(10, 4)
        self.assertTrue(not rect.contains(p))

    def test_RectHV_intersects_on_True(self):
        rect = RectHV(2, 10, 5, 10)
        rect2 = RectHV(7, 10, 4, 6)
        self.assertTrue(rect.intersects(rect2))

    def test_RectHV_intersects_on_False(self):
        rect = RectHV(2, 10, 5, 10)
        rect2 = RectHV(15, 20, 4, 6)
        self.assertTrue(not rect.intersects(rect2))

    def test_range_1_point(self):
        point_array = [[0.5, 0.7], [0.2, 0.8], [0.6, 0.4], [0.2, 0.2]]
        point_obj = PointSet(point_array)
        rect = RectHV(0.6, 1, 0.2, 0.5)
        points_in_rect = point_obj.range(rect)
        self.assertEqual([0.6, 0.4], [points_in_rect[0].x, points_in_rect[0].y])

    def test_range_2_points(self):
        point_array = [[0.5, 0.7], [0.2, 0.8], [0.6, 0.4], [0.2, 0.2], [0.5, 0.1], [0.4, 0.9], [0.7, 0.6]]
        point_obj = PointSet(point_array)
        rect = RectHV(0.4, 0.8, 0, 0.5)
        points_in_rect = point_obj.range(rect)
        self.assertEqual([0.6, 0.4, 0.5, 0.1], [points_in_rect[0].x, points_in_rect[0].y, points_in_rect[1].x, points_in_rect[1].y])