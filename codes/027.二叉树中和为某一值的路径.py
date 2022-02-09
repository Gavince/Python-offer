# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 上午8:04
# @Author  : gavin
# @FileName: 27.二叉树中和为某一值的路径.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入
整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点
形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

解决方案：
DFS
"""


class Solution:

    def FindPath(self, root, expectNumber):

        if root is None:
            return []

        res = []
        if root.val == expectNumber and root.left is None and root.right is None:
            res.append([root.val])

        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for path in left + right:
            # 向上添加路径
            res.append([root.val] + path)

        return res
