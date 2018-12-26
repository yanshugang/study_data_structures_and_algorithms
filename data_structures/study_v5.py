"""
使用数组实现Queue
"""


class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getattr__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._item[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class FullError(Exception):
    pass


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push()

    with pytest.raises(FullError) as excinfo:
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == size
