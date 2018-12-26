"""
替换空格

题目：
    请实现一个函数，将一个字符串中的空格替换成“%20”。
    例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    def find(self, s):
        return s.replace(" ", "%20")


def main():
    s = "We Are Happy."
    res_s = Solution().find(s)
    print(res_s)


if __name__ == '__main__':
    main()
