"""
树和二叉树

"""

node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


# 定义二叉树的节点类
class BinaryTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


# 定义二叉树
class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        node_dict = {}

        # 第一遍遍历，构造node节点
        for each in node_list:
            data = each["data"]  # A\B\...
            node_dict[data] = BinaryTreeNode(data)

        # 第二遍遍历，给根节点和子节点赋值
        for each in node_list:
            data = each["data"]
            node = node_dict[data]
            if each["is_root"]:
                root = node
            node.left = node_dict.get(each["left"])
            node.right = node_dict.get(each["right"])
        return cls(root)

    def pre_order_trav(self, subtree):
        """先序遍历"""
        if subtree is not None:
            print(subtree.data)  # 递归函数里先处理根
            self.pre_order_trav(subtree.left)  # 递归处理左子树
            self.pre_order_trav(subtree.right)  # 递归处理右子树

    def layer_trav(self, subtree):
        """层序遍历: 从根节点开始一层一层的遍历节点"""
        cur_nodes = [subtree]
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            cur_nodes = next_nodes  # 继续遍历下一层
            next_nodes = []

    def reverse(self, subtree):
        """反转二叉树"""
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


btree = BinaryTree.build_from(node_list)
btree.pre_order_trav(btree.root)
