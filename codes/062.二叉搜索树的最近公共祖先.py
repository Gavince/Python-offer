# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 上午8:51
# @Author  : gavin
# @FileName: 62.二叉搜索树的最近公共祖先.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

解题方法：
遍历
三种情况：
(1)两个指定节点在左右子数中；
(2)两个节点在左子树中；
(3)两个节点在右子树中。

返回条件:及不大于,也不小于
方法一：一次遍历
时间复杂度：O(N)
空间复杂度：O(1)

方法二：递归
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
"""


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

    def lowestCommonAncestorforDFS(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val < q.val and root.val < p.val:
            root = self.lowestCommonAncestorforDFS(root.right, p, q)
        if root.val > q.val and root.val > p.val:
            root = self.lowestCommonAncestorforDFS(root.left, p, q)
        return root
