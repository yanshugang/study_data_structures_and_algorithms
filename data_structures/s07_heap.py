# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/24 下午4:52

"""
堆是一种完全二叉树，有最大堆和最小堆两种。
    最大堆：对于每个非叶子节点v，v的值都比它的两个孩子大，称为最大堆特征。最大堆里的根总是存储最大值，最小的值存储在叶节点。
    最小堆：和最大堆相反，每个非叶子节点v，v的两个孩子的值都比它大。

parent = int((i-1) / 2)    # 取整
left = 2 * i + 1
right = 2 * i + 2

python内置heapq模块，用来实现堆的相关操作，原理是类似的。
"""

# 实现最大堆
from data_structures.s01_array import Array


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def _siftup(self, ndx):
        """
        向上筛选，递归交换直到满足最大堆特性。

        :param ndx:  接收一个位置
        """
        if ndx > 0:
            parent = int((ndx - 1) / 2)
            if self._elements[ndx] > self._elements[parent]:  # 如果插入的值大于父节点的值，就一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)  # 递归操作

    def _siftdown(self, ndx):
        """
        向下筛选，不断的和子节点进行交换，递归交换直到满足最大堆特性。

        :param ndx: 接收一个位置
        """
        left = 2 * ndx + 1  # 左子节点下标
        right = 2 * ndx + 2  # 右子节点下标
        # determine which node contains the larger value
        largest = ndx

        if (left < self._count  # 有左孩子
                and self._elements[left] >= self._elements[largest]
                and self._elements[left] >= self._elements[right]):  # 左孩子 > 右孩子
            largest = left

        elif (right < self._count  # 有右孩子
              and self._elements[right] >= self._elements[largest]):
            largest = right

        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)  # 递归操作

    def add(self, value):
        """添加元素"""
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)  # 维持堆的特性

    def extract(self):
        """提取最大值"""
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]  # 保存root值，root值即最大值
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下的节点放到root后siftDown
        self._siftdown(0)  # 维持堆特性
        return value  # 返回最大值


def test_maxheap():
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()
