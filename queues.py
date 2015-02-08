#Coursera Algorithms 1 - week 2
import unittest

class LinkedListNode(object):

    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, item):
       if self.head is None:
           self.head = LinkedListNode(item, next=None)
       else:
           self.head = LinkedListNode(item, next=self.head)

    def __iter__(self):
        return LinkedListIterate(self.head)

    def __repr__(self):
        repr_so_far = '<LinkedList with items '
        current = self.head
        while current is not None:
            if current != self.head:
                repr_so_far += ', '
            repr_so_far += str(current.item)
            current = current.next
        repr_so_far += '>'
        return repr_so_far

class LinkedListIterate(object):

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def next(self):
        if self.current is None:
            raise StopIteration()
        else:
            temp_current = self.current.item
            self.current = self.current.next
            return temp_current

# l = [1, 2]
# for x in l:
#     print str(x)
#
# iterator = l.__iter__()
# x = iterator.next()
# while x is not None:
#     print str(x)
#     x = iterator.next()

import random
class TestListLinked(unittest.TestCase):
    # def setUp(self):
    #     self.seq = range(10)

    def test_head_is_printed_properly_in_repr(self):
        to_add = 10
        l = LinkedList()
        l.push(to_add)
        self.assertEqual('<LinkedList with items {}>'.format(to_add), l.__repr__())

    def test_multiple_pushs(self):
        l = LinkedList()
        l.push(20)
        l.push(10)
        self.assertEqual('<LinkedList with items {}, {}>'.format(10, 20), l.__repr__())


    # def test_shuffle(self):
    #     # make sure the shuffled sequence does not lose any elements
    #     random.shuffle(self.seq)
    #     self.seq.sort()
    #     self.assertEqual(self.seq, range(10))
    #
    #     # should raise an exception for an immutable sequence
    #     self.assertRaises(TypeError, random.shuffle, (1,2,3))
    #
    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)
    #
    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)