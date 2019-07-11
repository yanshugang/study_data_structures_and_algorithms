"""
堆栈/栈 Stack
LIFO (last in first in)
push\pop
使用Deque实现stack
"""
from data_structures.s03_queue import Deque


class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class StrackUnderflow(ValueError):
    pass


# 使用deque实现stack
class Stack():
    def __init__(self):
        self.deque = Deque()  # 或者使用collection.deque

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


class SStrack():
    """栈的顺序表实现"""

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StrackUnderflow("in SStrack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StrackUnderflow("in SStrack.pop()")
        return self._elems.pop()


class LStrack():
    """栈的链接表实现"""

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StrackUnderflow("in LStrack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StrackUnderflow("")
        p = self._top
        self._top = p.next
        return p.elem


def test_stack():
    s = Stack()
    for i in range(3):
        s.push(i)

    assert len(s) == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert s.is_empty()

    # 测试异常
    import pytest
    with pytest.raises(Exception) as excinfo:
        s.pop()
    assert 'empty' in str(excinfo.value)
