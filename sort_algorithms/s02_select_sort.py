# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/24 下午6:07

"""
选择排序

每次站到最小的元素插入迭代的起始位置，这样每个位置从它自己的位置开始它就是最小的了。
可以理解为一个0到n-1的迭代，每次向后查找选择一个最小的元素。
"""
import random


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_idx = i  # 假设当前下标的元素是最小的
        for j in range(i + 1, n):  # 从i的后面开始找到最小的元素，得到它的下标
            if seq[j] < seq[min_idx]:
                min_idx = j  # 一个j循环下来之后就能找到了最小的元素它的下标

            if min_idx != i:
                seq[i], seq[min_idx] = seq[min_idx], seq[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
    assert seq == sorted(seq)
