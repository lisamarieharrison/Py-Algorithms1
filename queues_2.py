#Coursera Algorithms 1 - week 2, part 2
import unittest
import random

class LinkedListNode(object):

    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList(object):

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

    def enqueue(self, item):
       if self.head is None:
           self.head = LinkedListNode(item, next=None)
       else:
           self.head = LinkedListNode(item, next=self.head)

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Cannot remove item from empty list")
        item_index = random.randint(0, self.size())
        if self.head.next is None:
            random_item = self.head.item
            self.head = None
        else:
            current = self.head
            if item_index == 0:
                random_item = self.head.item
                self.head = self.head.next
            else:
                for i in range(0, item_index + 1):
                    if i == item_index - 1:
                        random_item = current.next.item
                        if item_index < self.size():
                            current.next = current.next.next
                        else:
                            current.next = None
                    current = current.next
        return random_item

    def sample(self):
        if self.isEmpty():
            raise RuntimeError("Cannot remove item from empty list")
        item_index = random.randint(0, self.size())
        current = self.head
        if item_index == 0:
            random_item = self.head.item
        else:
            for i in range(0, item_index + 1):
                if i == item_index - 1:
                    random_item = current.next.item
                current = current.next
        return random_item

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

    def test_head_is_printed_properly_in_repr(self):
        to_add = 10
        l = LinkedList()
        l.enqueue(to_add)
        self.assertEqual('<LinkedList with items {}>'.format(to_add), l.__repr__())

    def test_size_gets_correct_size_full_array(self):
        to_add = range(1, 21)
        l = LinkedList()
        for i in to_add:
            l.enqueue(i)
        self.assertEqual(len(to_add), l.size())

    def test_size_gets_correct_size_empty_array(self):
        l = LinkedList()
        self.assertEqual(0, l.size())

    def test_isEmpty_on_full_array(self):
        l = LinkedList()
        l.enqueue(1)
        self.assertEqual(False, l.isEmpty())

    def test_isEmpty_on_empty_array(self):
        l = LinkedList()
        self.assertEqual(True, l.isEmpty())

    def test_enqueue_adds_to_front(self):
        l = LinkedList()
        l.enqueue(10)
        l.enqueue(20)
        self.assertEqual('<LinkedList with items {}, {}>'.format(20, 10), l.__repr__())

    def test_dequeue_removes_an_item(self):
        to_add = range(1, 21)
        l = LinkedList()
        for i in to_add:
            l.enqueue(i)
        l.dequeue()
        l.dequeue()
        self.assertEqual(18, l.size())

    def test_dequeue_for_single_value(self):
        l = LinkedList()
        l.enqueue(1)
        random_item = l.dequeue()
        self.assertEqual(1, random_item)

    def test_dequeue_returns_int(self):
        to_add = range(1, 21)
        l = LinkedList()
        for i in to_add:
            l.enqueue(i)
        random_item = l.dequeue()
        self.assertEqual(True, isinstance(random_item, int))

    def test_sample_returns_int(self):
        to_add = range(1, 21)
        l = LinkedList()
        for i in to_add:
            l.enqueue(i)
        random_item = l.sample()
        self.assertEqual(True, isinstance(random_item, int))

    def test_sample_doesnt_remove_item(self):
        to_add = range(1, 21)
        l = LinkedList()
        for i in to_add:
            l.enqueue(i)
        random_item = l.sample()
        self.assertEqual(20, l.size())