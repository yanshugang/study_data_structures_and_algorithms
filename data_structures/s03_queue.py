"""
队列 FIFO (first in first out)
"""
from data_structures.s01_array import Array
from data_structures.s02_linked_list import LinkedList, CircualDoubleLinedList


class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    """使用单链表实现"""

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('queue full')
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_linked_list.popleft()


class ArrayQueue(object):
    """使用数组实现"""

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


class Deque(CircualDoubleLinedList):
    """使用双端链表实现双端队列"""

    def pop(self):
        if len(self) == 0:
            raise Exception('empty')

        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)

        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(value)

        return value


def test_queue():
    q = Queue()

    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.pop()
    assert 'empty' in str(excinfo.value)


def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push()

    with pytest.raises(FullError) as excinfo:
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == size
