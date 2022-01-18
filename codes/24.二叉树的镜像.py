# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 上午8:41
# @Author  : gavin
# @FileName: 24.二叉树的镜像.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
操作给定的二叉树，将其变换为源二叉树的镜像

解决方案：

源二叉树：
　　８
　６　10
5 7  9 11
镜像二叉树：
     8
  10  6
11  9  7  5
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def Mirror(self, root):
        if root is None:
            return None
        # 左右互换
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)

        return root
