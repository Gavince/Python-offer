# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 上午10:04
# @Author  : gavin
# @FileName: 37.二叉搜索树与双向链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

解题方法:
二叉搜索树的中序遍历是有序的
"""


class Solution:

    def treeToDoublyList(self, root):

        def dfs(cur):
            if not cur: return None
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root: return None
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head

        return self.head
