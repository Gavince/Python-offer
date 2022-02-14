# -*- coding: utf-8 -*-
# @Time    : 2021/8/8 下午3:20
# @Author  : gavin
# @FileName: 128.另一棵树的子树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有
相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。二叉树 tr
ee 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看
做它自身的一棵子树。

解题方法：
DFS

原题链接：https://leetcode-cn.com/problems/subtree-of-another-tree/
"""


class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        if not root and not subRoot:
            return True

        return self.isSameTree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)

    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2 or root1.val == root2.val:
            return False

        return self.isSameTree(root1.left, root2.left) \
               and self.isSameTree(root1.right, root2.right)
