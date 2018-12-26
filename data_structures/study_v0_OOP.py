class Bag(object):
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        # 选择数据结构很重要，需要满足实现ADT的基本操作。
        self._items = list()

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

