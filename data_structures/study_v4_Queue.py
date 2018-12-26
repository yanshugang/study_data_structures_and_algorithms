"""
队列 FIFO (first in first out)
使用单链表实现队列
"""


class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length

    def append(self, value):  # O(1)
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):  # O(1)
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        """遍历节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next

        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):  # O(n)
        """让他的前一个节点取执行他的下一个节点，然后del该节点"""
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                    del curnode
                    self.length -= 1
                    return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1  # 表明删除失效

    def find(self, value):  # O(n)
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):  # O(1)
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        """清除链表"""
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
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
