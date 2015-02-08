#Coursera Algorithms 1 - week 2
import unittest

class LinkedListNode(object):

    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList(object):

    def __init__(self):
        self.head = None

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
           self.head = LinkedListNode(item, next = None)
       else:
           self.head = LinkedListNode(item, next = self.head)

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
        return LinkedListIterate(self.head)

    def __repr__(self):
        repr_so_far = '<LinkedList with items '
        for i, current in enumerate(self):
            if i != 0:
                repr_so_far += ', '
            repr_so_far += str(current)
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

class TestListLinked(unittest.TestCase):
    # def setUp(self):
    #     self.seq = range(10)

    def test_head_is_printed_properly_in_repr(self):
        to_add = 10
        l = LinkedList()
        l.addFirst(to_add)
        self.assertEqual('<LinkedList with items {}>'.format(to_add), l.__repr__())

    def test_multiple_addFirsts(self):
        l = LinkedList()
        l.addFirst(20)
        l.addFirst(10)
        self.assertEqual('<LinkedList with items {}, {}>'.format(10, 20), l.__repr__())

    def test_removeFirst_for_two_items(self):
        l = LinkedList()
        l.addFirst(20)
        l.addFirst(10)
        l.removeFirst()
        self.assertEqual('<LinkedList with items {}>'.format(20), l.__repr__())

    def test_removeFirst_for_single_item(self):
        l = LinkedList()
        l.addFirst(20)
        l.removeFirst()
        self.assertEqual('<LinkedList with items >', l.__repr__())

    def test_removeFirst_for_empty_lists(self):
        l = LinkedList()
        self.assertRaises(RuntimeError, l.removeFirst)

    def test_isEmpty_on_empty_list(self):
        l = LinkedList()
        self.assertTrue(l.isEmpty())

    def test_isEmpty_on_full_list(self):
        l = LinkedList()
        l.addFirst(20)
        self.assertEqual(False, l.isEmpty())

    def test_size_on_full_array(self):
        l = LinkedList()
        for i in range(1, 21):
            l.addFirst(i)
        self.assertEqual(20, l.size())

    def test_size_on_empty_array(self):
        l = LinkedList()
        self.assertEqual(0, l.size())
