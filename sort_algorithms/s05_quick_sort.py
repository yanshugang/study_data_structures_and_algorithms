"""
快速排序

快速排序基于选择划分，是简单选择排序的优化。
每次划分将数据选到基准值两边，循环对两边的数据进行划分，类似于二分法。
算法的整体性能取决于划分的平均程度，即基准值的选择，此处衍生出快速排序的许多优化方案，甚至可以划分为多块。
基准值若能把数据分为平均的两块，划分次数O(logn)，每次划分遍历比较一遍O(n)，时间复杂度O(nlogn)。
额外空间开销出在暂存基准值，O(logn)次划分需要O(logn)个，空间复杂度O(logn)
"""


# 简单版本
def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    small = [i for i in array[1:] if i <= pivot]
    big = [i for i in array[1:] if i > pivot]

    return quick_sort(small) + [pivot] + quick_sort(big)


def main():
    array = [10, 12, 1, 4, 6, 22, 24, 5]
    res = quick_sort(array)
    print(res)


if __name__ == '__main__':
    main()
