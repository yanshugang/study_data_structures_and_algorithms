"""
二叉树

"""


class BinaryTreeNode(object):
    """定义二叉树的节点"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root
