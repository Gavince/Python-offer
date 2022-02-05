# -*- coding: utf-8 -*-
# @Time    : 2021/9/19 下午9:15
# @Author  : gavin
# @FileName: 149.路径总和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你二叉树的根节点root 和一个表示目标和的整数targetSum ，判断该树中是
否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和targetSum 。
叶子节点 是指没有子节点的节点。

解题方法：
DFS和BFS

原题链接：https://leetcode-cn.com/problems/path-sum/
"""

import collections


class Solution:
    def hasPathSumOfDFS(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum == root.val

        return self.hasPathSumOfDFS(root.left, targetSum - root.val) \
               or self.hasPathSumOfDFS(root.right, targetSum - root.val)


    def hasPathSumOfBFS(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        deque = collections.deque([(root, root.val)])
        while deque:

            root, path = deque.popleft()
            if not root.left and not root.right and targetSum == path:
                return True

            if root.left:
                deque.append((root.left, root.left.val + path))
            if root.right:
                deque.append((root.right, root.right.val + path))

        return False