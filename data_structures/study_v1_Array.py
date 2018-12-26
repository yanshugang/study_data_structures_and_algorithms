"""
线性结构：内存连续，可以通过下标访问
类型：数组(array)和列表(list)

用list实现定长的array
"""


# python的array: 只能存同一类型（数值或字符），更推荐使用numpy.array

class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getattr__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
