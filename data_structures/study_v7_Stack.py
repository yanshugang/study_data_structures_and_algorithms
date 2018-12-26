"""
栈 stack
LIFO (last in first in)
push\pop
使用Deque实现stack
"""


class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircualDoubleLinedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        # 创建一个根节点，自己指向自己，是一个闭环
        node = Node()
        node.next, node.prev = node, node
        self.root = node

        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        # 首先检查是否超长
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full')
        node = Node(value=value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node

        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full')
        node = Node(value=value)

        if self.root.next is self.root:  # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node

        self.length += 1

    def remove(self, node):  # O(1)
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev  # tailnode
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


# 实现双端队列
class Deque(CircualDoubleLinedList):
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
