# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 上午8:30
# @Author  : gavin
# @FileName: 23.树的子结构.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

解决方案：
①如果A,B有一个为空，return False
②如果A,B不为空，A.val == B.val, 且B为单节点，则return True;如果结点B不为单节点则需要比较
A.left.val == B.left.val 和 A.right.val == B.right.val
③如果B.val != A.val 则遍历Ａ结点的子节点和B进行比较，找到相同结点后，转②，否则return False
"""
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    # 方法一
    def HasSubtree(self, pRoot1, pRoot2):

        if pRoot1 is None or pRoot2 is None:
            return False

        def has_equal(pRoot1, pRoot2):
            """存在相等的结点"""
            if pRoot2 is None:
                return True
            if pRoot1 is None:
                return False

            if pRoot1.val == pRoot2.val:
                if pRoot2.left is None:
                    left_equal = True
                else:
                    left_equal = has_equal(pRoot1.left, pRoot2.left)
                if pRoot2.right is None:
                    right_equal = True
                else:
                    right_equal = has_equal(pRoot1.right, pRoot2.right)

                return right_equal and left_equal

            return False

            if pRoot1.val == pRoot2.val:
                ret = has_equal(pRoot1, pRoot2)
                if ret:
                    return True
            ret = self.HasSubtree(pRoot1.left, pRoot2)
            if ret:
                return True
            ret = has_equal(pRoot1.right, pRoot2)

            return ret

    def HasSubTree(self, pRoot1, pRoot2):

        if pRoot1 is None or pRoot2 is None:
            return False
        return self.isSubTree(pRoot1, pRoot2)

    def isSubTree(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True

        if pRoot1 is None:
            return False
        if pRoot2 is None:
            return False

        if pRoot1.val == pRoot2.val:
            if pRoot2.left is None and pRoot2.right is None:  # 此时pRoot2无子节点
                return True
            else:
                if self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right):
                    return True

        # A,B树原始根结点不相同
        return self.isSubTree(pRoot1.left, pRoot2) or self.isSubTree(pRoot1.right, pRoot2)

    # 方法二
    def isSubstructure(self, A, B):

        # A,B 不都为空
        if not A or not B:
            return False

        # 先序遍历，寻找子结构
        return self.isInclude(A, B) or self.isSubstructure(A.left, B) or self.isSubstructure(A.right, B)

    def isInclude(self, A, B):

        # B优先遍历完，且为子结构
        if not B:
            return True
        #　A优先遍历完，且不存在子结构
        if not A or A.val != B.val:
            return False
        # 递归寻找匹配
        return self.isInclude(A.left, B.left) and self.isInclude(A.right, B.right)
