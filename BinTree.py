from operator import *

# 二叉树结点
class TreeNode:
    def __init__(self, value, lchild = None, rchild = None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class BinTree:
    def __init__(self):
        self.node_list = []
        self.expr_list = []


    def generate(self, expr):
        """
        根据输入的表达式创建二叉树
        :param expr: 列表类型的表达式
        :return:
        """
        self.expr_list = expr
        for item in expr:
            parent = TreeNode(item)
            if not item in ['+', '-', 'x', '÷']:
                self.node_list.append(parent)
            else:
                rchild = self.node_list.pop()
                lchild = self.node_list.pop()
                parent.lchild = lchild
                parent.rchild = rchild
                self.node_list.append(parent)

        return self.node_list[-1]

    def isEqual(self, root):
        """
        递归遍历二叉树，判断两个二叉树是否相同
        :param root:
        :return:
        """
        if not root.lchild:
            if not root.rchild:
                return root.value
        elif root.value == '+' or root.value == 'x':
            lchild = self.isEqual(root.lchild)
            rchild = self.isEqual(root.rchild)
            if le(lchild, rchild):
                return root.value + lchild + rchild
            else:
                return root.value + rchild + lchild
        else:
            return root.value + self.isEqual(root.lchild) + self.isEqual(root.rchild)