# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 上午8:21
# @Author  : gavin
# @FileName: 136.二叉树的右视图.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返
回从右侧所能看到的节点值。

解题方法：
层序遍历
"""
import collections


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if root is None:
            return []
        res = []
        deque = collections.deque([root])
        while deque:
            tmp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                tmp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(tmp[-1])

        return res