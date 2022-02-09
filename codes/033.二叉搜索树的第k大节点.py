# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 上午9:47
# @Author  : gavin
# @FileName: 33.二叉搜索树的第k大节点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给定一棵二叉搜索树，请找出其中第k大的节点。
解决方法：
二叉搜索树的中序遍历为有序序列（递增序列），将其转换为逆序列，可以求得最大kth数值。
"""


class Solution:

    def kthLargest(self, root, k):

        def dfs(root):
            """右根左遍历"""
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
