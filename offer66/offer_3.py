"""
从尾到头打印链表

题目：
    输入一个链表，从尾到头打印链表每个节点的值。
"""


# todo: 对链表理解不透彻
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方案一：
#   使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
#   这个方法效率应该还可以，先存入vector，再反转vector
class Solution:
    def print_list_from_tail_to_head(self, list_node):
        if not list_node:
            return []

        result = []
        while list_node.next is not None:
            result.extend([list_node.val])
            list_node = list_node.next
        result.extend([list_node.val])

        return result[::-1]


# 方案二：
#   使用insert直接在头部插入
class Solution2:
    def print_list_from_tail_to_head(self, list_node):
        if not list_node:
            return []

        result = []
        head = list_node

        while head:
            result.insert(0, head.val)
            head = head.next
        return result
