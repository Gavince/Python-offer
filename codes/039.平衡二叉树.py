# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 上午10:10
# @Author  : gavin
# @FileName: 39.平衡二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
题目描述：
    给定一个二叉树，判断它是否是高度平衡的二叉树。本题中，一棵高度平衡二叉树定
义为：一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

解题方法：
    二叉树的每个节点的左右子树的高度差的绝对值不超过 1，则二叉树是平衡二叉树
。根据定义，一棵二叉树是平衡二叉树，当且仅当其所有子树也都是平衡二叉树，因此可
以使用递归的方式判断二叉树是不是平衡二叉树，递归的顺序可以是自顶向下或者自底向
上，其中自低向上复杂度最优。

原题链接:https://leetcode-cn.com/problems/balanced-binary-tree/
"""


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return - 1
            else:
                return max(left_height, right_height) + 1

        return height(root) >= 0
