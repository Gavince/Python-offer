# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 下午4:03
# @Author  : gavin
# @FileName: 202.N叉树的最大深度.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个 N 叉树，找到其最大深度。最大深度是指从根节点到最远叶子节点
的最长路径上的节点总数。N叉树输入按层序遍历序列化表示，每组子节点由空值
分隔（请参见示例）。

解题方法：
BFS和DFS

原题链接：https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/solution/n-cha-shu-de-zui-da-shen-du-by-leetcode-n7qtv/
"""


class Solution:
    def maxDepthforBFS(self, root: 'Node') -> int:

        if root is None:
            return 0
        deque = [root]
        ans = 0
        while deque:
            deque = [child for node in deque for child in node.children]
            ans += 1
        return ans

    def maxDepthforDFS(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        return max(self.maxDepthforDFS(child) + 1 for child in root.children)