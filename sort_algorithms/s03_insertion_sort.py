# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/7/24 下午6:07

"""
插入排序

每次挑选下一个元素插入已经排序的数组中，初始时已排序数组只有一个火元素。
"""


def insertion_sort(seq):
    n = len(seq)
    print(seq)
    for i in range(1, n):
        value = seq(i)  # 保存当前位置的值， 因为转移的过程中它的位置可能被覆盖
        # 找到这个值的合适位置，使得前边的数组有序，即[0, i]是有序的
        pos = i

        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]  # 如果前边的元素比它大，就让它一直前移
            pos -= 1
        seq[pos] = value
        print(seq)


def test_insertion_sort():
    pass
