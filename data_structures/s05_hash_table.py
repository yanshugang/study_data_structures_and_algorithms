"""
使用数组实现哈希表
"""


class Array(object):
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, index):
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


class Slot(object):
    """定义一个hash表数组的槽
    注意，一个槽有三种状态，看你能否想明白
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None  # 没有被使用过
    EMPTY = Slot(None, None)  # 使用过又被删除了

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def __len__(self):
        return self.length

    def __iter__(self):
        # 遍历操作，只遍历key
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key

    @property
    def _load_factor(self):
        # 负载因子
        return self.length / float(len(self._table))

    def _hash(self, key):
        # hash函数
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        # 查找某个元素的位置
        index = self._hash(key)
        _len = len(self._table)
        # 解决哈希冲突
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index * 5 + 1) % _len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        # 判断该位置是否可以插入
        return self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED

    def _find_slot_for_insert(self, key):
        # 寻找插入位置
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def _rehash(self):
        # 重哈希
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:  # 当负载因子超过0.8时，需要重新开辟空间
                self._rehash()
            return True

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1
        self._table[index] = HashTable.EMPTY
        return value


# 使用hash表实现字典
class DictADT(HashTable):
    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_hash_table():
    h = HashTable()
    h.add("a", 0)
    h.add("b", 1)
    h.add("c", 2)
    assert len(h) == 3
    assert h.get("a") == 0
    assert h.get("d") is None

    h.remove("a")
    assert h.get("a") is None
    assert sorted(list(h)) == ["b", "c"]


def test_dict_adt():
    import random
    d = DictADT()

    d["a"] = 1
    assert d["a"] == 1

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)
