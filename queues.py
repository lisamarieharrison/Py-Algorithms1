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

    def addLast(self, item):
        if self.head is None:
            self.head = DequeNode(item, next=None, previous=None)
            self.tail = self.head
        else:
            self.tail.next = DequeNode(item, next=None, previous=self.tail)
            self.tail = self.tail.next

    def removeFirst(self):
        if self.isEmpty():
            raise RuntimeError("Cannot remove item from empty list")
        first_item = self.head.item
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        return first_item

    def removeLast(self):
        if self.isEmpty():
            raise RuntimeError("Cannot remove item from empty list")
        last_item = self.tail.item
        if self.tail.previous is None:
            self.head = None
            self.tail = None
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous
        return last_item

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
    # def setUp(self):
    #     self.seq = range(10)

    def test_head_is_printed_properly_in_repr(self):
        to_add = 10
        l = Deque()
        l.addFirst(to_add)
        self.assertEqual('<Deque with items {}>'.format(to_add), l.__repr__())

    def test_multiple_addFirsts(self):
        l = Deque()
        l.addFirst(20)
        l.addFirst(10)
        self.assertEqual('<Deque with items {}, {}>'.format(10, 20), l.__repr__())

    def test_multiple_addLast(self):
        l = Deque()
        l.addLast(20)
        l.addLast(10)
        self.assertEqual('<Deque with items {}, {}>'.format(20, 10), l.__repr__())

    def test_addFirst_and_addLast(self):
        l = Deque()
        l.addFirst(20)
        l.addLast(10)
        l.addFirst(5)
        self.assertEqual('<Deque with items {}, {}, {}>'.format(5, 20, 10), l.__repr__())

    def test_removeFirst_for_two_items(self):
        l = Deque()
        l.addFirst(20)
        l.addFirst(10)
        l.removeFirst()
        self.assertEqual('<Deque with items {}>'.format(20), l.__repr__())

    def test_removeFirst_for_single_item(self):
        l = Deque()
        l.addFirst(20)
        l.removeFirst()
        self.assertEqual('<Deque with items >', l.__repr__())

    def test_removeLast_for_single_item(self):
        l = Deque()
        l.addFirst(20)
        l.removeLast()
        self.assertEqual('<Deque with items >', l.__repr__())

    def test_removeLast_for_two_items(self):
        l = Deque()
        l.addFirst(20)
        l.addFirst(10)
        l.removeLast()
        self.assertEqual('<Deque with items {}>'.format(10), l.__repr__())

    def test_removeFirst_return(self):
        l = Deque()
        l.addFirst(20)
        l.addFirst(10)
        self.assertEqual(10, l.removeFirst())

    def test_removeLast_return(self):
        l = Deque()
        l.addFirst(20)
        l.addFirst(10)
        self.assertEqual(20, l.removeLast())

    def test_removeFirst_for_empty_lists(self):
        l = Deque()
        self.assertRaises(RuntimeError, l.removeFirst)

    def test_combination_add_and_remove(self):
        l = Deque()
        l.addFirst(20)
        l.addFirst(10)
        l.addLast(5)
        l.removeFirst()
        l.addLast(30)
        l.removeLast()
        self.assertEqual('<Deque with items {}, {}>'.format(20, 5), l.__repr__())

    def test_isEmpty_on_empty_list(self):
        l = Deque()
        self.assertTrue(l.isEmpty())

    def test_isEmpty_on_full_list(self):
        l = Deque()
        l.addFirst(20)
        self.assertEqual(False, l.isEmpty())

    def test_size_on_full_array(self):
        l = Deque()
        for i in range(1, 21):
            l.addFirst(i)
        self.assertEqual(20, l.size())

    def test_size_on_empty_array(self):
        l = Deque()
        self.assertEqual(0, l.size())
