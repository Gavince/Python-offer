# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 上午9:55
# @Author  : gavin
# @FileName: 152.验证二叉搜索树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

解题方法：
BFS和DFS
"""


class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:

        if root is None: False

        deque = []
        cur = root
        pre_val = float("-inf")
        while deque or cur:
            while cur:
                deque.append(cur)
                cur = cur.left

            node = deque.pop()
            if node.val <= pre_val:
                return False
            pre_val = node.val
            cur = node.right

        return True

class Solution2:
    def __init__(self):
        self.pre = float('-inf')
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None: return True
        if not self.isValidBST(root.left): return False
        if root.val <= self.pre:  return False
        self.pre = root.val
        return self.isValidBST(root.right)