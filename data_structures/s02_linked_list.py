"""
链表
    单链表
    双链表

+ = = = = = = = +
| append | O(1) |
+ — — — — — — — +
| remove | O(1) |
+ - - - - - - - +
| search | O(n) |
+ = = = = = = = +

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


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    ll.remove(0)
    assert len(ll) == 2
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.appendleft(0)
    assert list(ll) == [0, 1, 2]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 2]

    ll.clear()
    assert len(ll) == 0


def test_double_link_list():
    dll = CircualDoubleLinedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
