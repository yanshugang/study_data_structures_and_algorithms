"""
栈的顺序表实现
"""


class StrackUnderflow(ValueError):
    pass


class SStrack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StrackUnderflow("in SStrack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StrackUnderflow("in SStrack.pop()")
        return self._elems.pop()
