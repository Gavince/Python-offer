# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 上午8:51
# @Author  : gavin
# @FileName: 62.二叉搜索树的最近公共祖先.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 设立标准
        if p.val > q.val:
            p, q = q, p
        # 遍历
        while root:

            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                break

        return root
