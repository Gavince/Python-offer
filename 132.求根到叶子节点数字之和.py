# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 上午8:19
# @Author  : gavin
# @FileName: 132.求根到叶子节点数字之和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0
到 9 之间的数字。每条从根节点到叶节点的路径都代表一个数字：例如
，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。计算从根
节点到叶节点生成的 所有数字之和 。叶节点是指没有子节点的节点。

解题方法：
DFS 和　BFS
时间复杂度：O(N)
空间复杂度：O(N)
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(root, sum):

            if root is None:
                return 0
            elif root.left is None and root.right is None:
                return 10 * sum + root.val

            return dfs(root.left, 10 * sum + root.val) + dfs(root.right, 10 * sum + root.val)

        return dfs(root, 0)

    # BFS
    def sumNumbers(self, root: TreeNode) -> int:

        if not root:
            return 0

        total = 0
        node_deque = collections.deque([root])
        val_deque = collections.deque([root.val])

        while node_deque:
            node = node_deque.popleft()
            num = val_deque.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                # 每一节点存储到当前节点的加和值，并和节点一一对应
                if left:
                    node_deque.append(left)
                    # 当前值乘以进位（每一层作为一个进位）
                    val_deque.append(num * 10 + left.val)
                if right:
                    node_deque.append(right)
                    val_deque.append(num * 10 + right.val)

        return total
