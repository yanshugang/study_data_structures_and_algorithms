# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/23 下午7:20

"""
优先队列
    正常进入，按照优先级出。

    实现机制：
        1、使用堆实现
        2、使用二叉搜索树实现

    一般不要求自己实现。
"""
from data_structures.s07_heap import MaxHeap


class PriorityQueeu(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self._maxheap = MaxHeap(max_size)  # TODO：使用最大堆实现排序， 需要先看堆排序。

    def push(self, priority, value):
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueeu(size)
    pq.push(5, "purple")
    pq.push(0, "white")
    pq.push(3, "organge")
    pq.push(1, "black")

    res = []

    while not pq.is_empty():
        res.append(pq.pop())

    assert res == ["purple", "white", "organge", "black"]
