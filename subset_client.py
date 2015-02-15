#Coursera Algorithms 1 - week 2, part 2
import unittest
import random
import numpy as np

class Array(object):

    def __init__(self, str = None):
        self.Array = np.empty((0, ))
        self.sz = 0
        if str is not None:
            self.Array = str
            self.sz = len(str)

    def isEmpty(self):
        if self.sz == 0:
            return True
        else:
            return False

    def size(self):
        return self.sz

    def length(self):
        return len(self.Array)

    def enqueue(self, item):
        if self.sz == len(self.Array):
            if self.sz == 0:
                temp = np.zeros(1, dtype = int)
            else:
                temp = np.zeros(self.sz*2, dtype = int)
                temp[0:self.sz] = self.Array
            self.Array = temp
        self.Array[self.sz] = item
        self.sz += 1

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Cannot remove item from empty list")
        item_index = random.randint(0, self.size() - 1)
        random_item = self.Array[item_index]
        self.Array[item_index] = self.Array[self.sz - 1]
        self.Array[self.sz - 1] = 0
        self.sz -= 1
        if self.sz < len(self.Array)*0.5:
            self.Array = self.Array[0:self.sz]
        return random_item

    def sample(self):
        if self.isEmpty():
            raise RuntimeError("Cannot get item from empty list")
        item_index = random.randint(0, self.size() - 1)
        random_item = self.Array[item_index]
        return random_item

    def __iter__(self):
        return ArrayIterate(self.Array)

    def __repr__(self):
        repr_so_far = '<Array with items '
        for i, current in enumerate(self):
            if i != 0:
                repr_so_far += ', '
            repr_so_far += str(current)
        repr_so_far += '>'
        return repr_so_far

class ArrayIterate(object):

    def __init__(self, obj):
        self.obj = obj
        self.current = 0

    def __iter__(self):
        return self

    def next(self):
        if self.current == len(self.obj):
            raise StopIteration()
        else:
            temp_current = self.obj[self.current]
            self.current = self.current + 1
            return temp_current

class Subset(object):

    def returnSubset(self, k, str):
        if k > str.size():
            raise RuntimeError("k cannot be greater than the length of str")
        i = 1
        while i <= k:
            print str.dequeue(),
            i += 1

class TestListLinked(unittest.TestCase):

    def test_head_is_printed_properly_in_repr(self):
        to_add = 10
        l = Array()
        l.enqueue(to_add)
        self.assertEqual('<Array with items {}>'.format(to_add), l.__repr__())

    def test_size_gets_correct_size_full_array(self):
        to_add = range(1, 21)
        l = Array()
        for i in to_add:
            l.enqueue(i)
        self.assertEqual(20, l.size())

    def test_size_gets_correct_size_empty_array(self):
        l = Array()
        self.assertEqual(0, l.size())

    def test_isEmpty_on_full_array(self):
        l = Array()
        l.enqueue(1)
        self.assertEqual(False, l.isEmpty())

    def test_isEmpty_on_empty_array(self):
        l = Array()
        self.assertEqual(True, l.isEmpty())

    def test_enqueue_adds_to_back(self):
        l = Array()
        l.enqueue(10)
        l.enqueue(20)
        self.assertEqual('<Array with items {}, {}>'.format(10, 20), l.__repr__())

    def test_dequeue_removes_item(self):
        to_add = range(1, 21)
        l = Array()
        for i in to_add:
            l.enqueue(i)
        l.dequeue()
        self.assertEqual(19, l.size())

    def test_dequeue_returns_int(self):
        to_add = range(1, 21)
        l = Array()
        for i in to_add:
            l.enqueue(i)
        item = l.dequeue()
        self.assertTrue(isinstance(item, int))

    def test_dequeue_resizes_array(self):
        to_add = range(1, 6)
        l = Array()
        for i in to_add:
            l.enqueue(i)
        l.dequeue() #has size 8
        l.dequeue() #resizes back to 3
        self.assertTrue(l.length() == 3)

    def test_sample_returns_int(self):
        to_add = range(1, 10)
        l = Array()
        for i in to_add:
            l.enqueue(i)
        item = l.sample()
        self.assertTrue(isinstance(item, int))

    def test_sample_doesnt_remove(self):
        to_add = range(1, 10)
        l = Array()
        for i in to_add:
            l.enqueue(i)
        start_length = l.size()
        l.sample()
        end_length = l.size()
        self.assertEqual(start_length, end_length)

    def test_subset(self):
        str = np.array(range(1, 21))
        str = Array(str)
        sub = Subset()
        sub.returnSubset(11, str)
        self.assertEqual(9, str.size())

    def test_subset_error_k_larger_N(self):
        str = np.array(range(1, 5))
        str = Array(str)
        sub = Subset()
        self.assertRaises(RuntimeError, sub.returnSubset, 11, str)