# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午4:58
# @Author  : gavin
# @FileName: 108. 把二叉树搜索树装换为累加树.py.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给出二叉搜索树的根节点，该树的节点值各不相同，请你将其转换为累加树（
Greater Sum Tree），使每个节点 node的新值等于原树中大于或等于node.val
的值之和。

解题方法：
二叉搜索树中序遍历，其遍历方向为：
left-->right：由小到大
right-->left:由大到小

时间复杂度：O(n)
空间复杂度：O(n)
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root is None:
                return

            dfs(root.right)
            root.val += self.num
            self.num = root.val
            dfs(root.left)
            return root
        # 保存当前节点的累加值
        self.num = 0

        return dfs(root)
