"""
二维数组中的查找

题目：
    在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""


# 方案一：直接遍历
class solution_1:
    def find(self, array, elem):
        if not array:
            raise Exception("搞啥呢")
        row = len(array)
        col = len(array[0])

        for i in range(row):
            for j in range(col):
                if elem == array[i][j]:
                    return True
        return False


# 方案二：从右上或者左下开始遍历，夹逼
class solution_2():
    def find(self, array, elem):
        if not array:
            raise Exception("搞啥呢")

        row = len(array)
        col = len(array[0])

        i = 0
        j = col - 1

        while i < row and j >= 0:
            if array[i][j] > elem:
                j -= 1
            elif array[i][j] < elem:
                i += 1
            else:
                return True

        return False


def main():
    a_array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    b_array = []
    is_exist = solution_2().find(array=a_array, elem=12)
    print(is_exist)


if __name__ == '__main__':
    main()
