"""
栈的链接表实现
"""


class StrackUnderflow(ValueError):
    pass


class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStrack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StrackUnderflow("in LStrack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StrackUnderflow("")
        p = self._top
        self._top = p.next
        return p.elem
