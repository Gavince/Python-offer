# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 上午8:14
# @Author  : gavin
# @FileName: 133.二叉树的中序遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个二叉树的根节点 root ，返回它的中序遍历。

解题方法：
(1)递归
(2)遍历

原题链接：
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""

        res = []

        def dfs(root):
            if root is None:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return root

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            tmp_node = stack.pop()
            res.append(tmp_node.val)
            cur = tmp_node.right

        return res