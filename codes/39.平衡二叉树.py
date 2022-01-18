# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 上午10:10
# @Author  : gavin
# @FileName: 39.平衡二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
题目描述：
给定一个二叉树，判断它是否是高度平衡的二叉树。

解题方法：
二叉树的每个节点的左右子树的高度差的绝对值不超过 1，则二叉树是平衡二叉树。根据定义，一棵二叉树是平衡二叉树，
当且仅当其所有子树也都是平衡二叉树，因此可以使用递归的方式判断二叉树是不是平衡二叉树，递归的顺序可以是自顶向
下或者自底向上，其中自低向上复杂度最优。
"""


class Solution:

    def isBalanced(self, root) -> bool:
        def height(root):
            if not root: return 0
            leftHight = height(root.left)
            rightHight = height(root.right)
            if leftHight == -1 or rightHight == -1 or abs(leftHight - rightHight) > 1:
                return -1
            else:
                # 求解当前结点的高度
                return max(leftHight, rightHight) + 1

        return height(root) >= 0
