# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 上午9:16
# @Author  : gavin
# @FileName: 35.二叉树的深度.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径
，最长路径的长度为树的深度。

实例：
给定二叉树 [3,9,20,null,null,15,7]，
深度: 3

解法：
(1)后续遍历DFS
二叉树的深度=max(左子树的深度，右子树的深度) + 1
(2)层序遍历(BFS)
每一层的结点单独进行遍历，并设置计数

知识点：
树中的一个节点的深度是它到根节点的路径上的边的条数
1> 一棵树只有一个节点或没有节点，它的深度是0；
2> 二叉树的根节点只有左子树而没有右子树，那么可以判断，二叉树的深度应该是其左子树的深度加1；
3> 二叉树的根节点只有右子树而没有左子树，那么可以判断，那么二叉树的深度应该是其右树的深度加1；
4> 二叉树的根节点既有右子树又有左子树，那么可以判断，那么二叉树的深度应该是其左右子树的深度较大值加1。
"""
import collections


class Solution:

    def maxDepth1(self, root: TreeNode) -> int:
        """后序遍历"""

        if not root: return 0

        return max(self.maxDepth1(root.left), self.maxDepth1(root.right)) + 1

    def maxDepth2(self, root: TreeNode) -> int:

        if root is None: return 0
        deque = collections.deque([root])
        depth = 0
        while deque:
            for _ in range(len(deque)):
                node = deque.popleft()
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            depth += 1

        return depth
