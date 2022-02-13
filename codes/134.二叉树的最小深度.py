# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 上午9:35
# @Author  : gavin
# @FileName: 134.二叉树的最小深度.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    给定一个二叉树，找出其最小深度。最小深度是从根节点到最近叶子节点的最短
路径上的节点数量。说明：叶子节点是指没有子节点的节点。

解题方法：
递归和非递归

原题链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
"""
import collections


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return 1 + min_depth

    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        deque = collections.deque([(root, 1)])
        while deque:
            node, depth = deque.popleft()
            # 第一个叶子结点
            if node.left is None and node.right is None:
                return depth
            if node.left: deque.append((node.left, depth + 1))
            if node.right: deque.append((node.right, depth + 1))