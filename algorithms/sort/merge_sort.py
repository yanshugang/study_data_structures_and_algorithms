"""
归并排序
运用分治递归思想：将大问题分为较小的子问题，分而治之；递归调用同样的方法解决子问题。最终将序列的排序问题分治为一个数的排序问题，关键在于如何将子问题答案合并为问题答案。
两个有序序列合并为一个有序序列，借助一个暂存数组（列表），两个序列元素依次比较填入暂存列表，形成一个有序序列。
归并排序划分子问题采用二分法，共需O(logn)次划分，当然需要相当次合并；每次合并遍历比较O(n)。时间复杂度O(nlogn)。
额外空间开销出在合并过程中的一个暂存数组，空间复杂度O(n)。

1、分解：原问题为若干子问题，这些子问题是原问题的规模最小的实例
2、解决：这些子问题，递归地求解这些子问题。当子问题的规模足够小，就可以直接求解
3、合并：这些子问题的解成原问题的解
"""


def merge_sorted_list(sorted_a, sorted_b):
    # todo: 没看懂
    """合并两个有序序列，返回一个新的有序序列"""
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    # 最后别忘记把多余的都放到有序数组里
    while a < length_a:
        new_sorted_seq.append(sorted_a[a])
        a += 1

    while b < length_b:
        new_sorted_seq.append(sorted_b[b])
        b += 1

    return new_sorted_seq


def merge_sort(seq):
    if len(seq) <= 1:  # 递归出口
        return seq
    else:
        mid = int(len(seq) / 2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])

        # 合并有序数组
        return merge_sorted_list(left_half, right_half)


def main():
    array = [10, 12, 1, 4, 6, 22, 24, 5]
    res = merge_sort(array)
    print(res)
 

if __name__ == '__main__':
    main()
