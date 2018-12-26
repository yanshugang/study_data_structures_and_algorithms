"""
冒泡排序

冒泡排序对数据操作n-1轮，每轮找出一个最大（小）值。
操作只对相邻两个数比较与交换，每轮会将一个最值交换到数据列首（尾），像冒泡一样。
每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。
额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)。
"""


def bubble_sort(l):
    l_length = len(l)
    if l_length <= 1:
        return l

    for i in range(0, l_length-1):
        print(l)
        for j in range(0, l_length - 1 - i):  # 这里之所以 n-1 还需要 减去 i 是因为每一轮冒泡最大的元素都会冒泡到最后，无需再比较
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


def test():
    l = [3, 4, 5, 0, 9, 1, 7, 8, 6, 2]
    print(l)
    l_res = bubble_sort(l)
    print(l_res)


if __name__ == '__main__':
    test()
