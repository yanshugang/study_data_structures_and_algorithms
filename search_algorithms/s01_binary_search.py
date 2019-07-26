"""
二分查找
必须是有序数组
时间复杂度：O(logn)

算法思想：
1、获取数组中间位置-mid
2、拿待查找值和中间值比较，如果
"""


def binary_search(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1

    while beg <= end:
        # 计算数组中间位置
        mid = int((beg + end) / 2)  # beg + (end-beg)/2

        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1

    return -1


def test_binary_search():
    # assert 0
    a = list(range(10))

    # 如何设置测试用例:(正常值、异常值、边界值)

    # 正常值
    assert binary_search(a, 1) == 1

    # 异常值
    assert binary_search(None, 1) == -1
    assert binary_search(a, -1) == -1

    # 边界值
    assert binary_search(a, 0) == 0

    # TDD，测试驱动开发
