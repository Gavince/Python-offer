# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 上午8:48
# @Author  : gavin
# @FileName: 61.二叉树的最近公共祖先.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。百度百科中最近公共祖先的定
义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q
的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

解题方法：
DFS

原题链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
"""


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # 回朔终点
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 三种情况
        if not left: return right
        if not right: return left

        return root