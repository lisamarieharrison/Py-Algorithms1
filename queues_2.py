#Coursera Algorithms 1 - week 2
import unittest

class DequeNode(object):

    def __init__(self, item, next, previous):
        self.item = item
        self.next = next
        self.previous = previous

class Deque(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        sz = 0
        for i, current in enumerate(self):
            sz += 1
        return sz

    def addFirst(self, item):
       if self.head is None:
           self.head = DequeNode(item, next=None, previous=None)
           self.tail = self.head
       else:
           self.head.previous = DequeNode(item, next=self.head, previous=None)
           self.head = self.head.previous

    def removeFirst(self):
        if self.isEmpty():
            raise RuntimeError("Cannot remove item from empty list")
        first_item = self.head.item
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        return first_item

    def __iter__(self):
        return DequeIterate(self.head)

    def __repr__(self):
        repr_so_far = '<Deque with items '
        for i, current in enumerate(self):
            if i != 0:
                repr_so_far += ', '
            repr_so_far += str(current)
        repr_so_far += '>'
        return repr_so_far

class DequeIterate(object):

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

class TestListLinked(unittest.TestCase):

    def test_head_is_printed_properly_in_repr(self):
        to_add = 10
        l = Deque()
        l.addFirst(to_add)
        self.assertEqual('<Deque with items {}>'.format(to_add), l.__repr__())
