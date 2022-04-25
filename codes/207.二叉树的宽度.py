# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 上午8:27
# @Author  : gavin
# @FileName: 207.二叉树的宽度.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二
叉树与满二叉树（full binary tree）结构相同，但一些节点为空。每一层的宽度被定义为两个端点
（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度

解题方法：
BFS和DFS
需要记录每一层的深度和结点所在的位置

BFS:
时间复杂度：O(N) 其中 N 是输入树的节点数目，我们遍历每个节点一遍
空间复杂度：O(N) 这是 queue 的大小
DFS:
时间复杂度：O(N) 其中 N 是输入树的节点数目，我们遍历每个节点一遍
空间复杂度：O(N) 这部分空间是因为我们 DFS 递归过程中有 N 层的栈

原题链接：https://leetcode-cn.com/problems/maximum-width-of-binary-tree/
"""


class Solution:
    def widthOfBinaryTreeofBFS(self, root: Optional[TreeNode]) -> int:

        if not root: return 0
        deque = [(root, 0, 0)]
        cur_depth, depth, left = 0, 0, 0
        ans = 0
        while deque:
            root, depth, pos = deque.pop(0)
            # 只能进行同层结点之间的宽度比较
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(ans, pos - left + 1)
            # 　进入下一层结点的计算
            if root.left:
                deque.append((root.left, depth + 1, pos * 2))
            if root.right:
                deque.append((root.right, depth + 1, pos * 2 + 1))
        return ans

    def widthOfBinaryTreeofDFS(self, root: Optional[TreeNode]) -> int:

        if root is None: return 0
        # 存每一层的最左结点的位置
        left = {}
        self.ans = 0

        def dfs(root, depth, pos):
            if root:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(root.left, depth + 1, pos * 2)
                dfs(root.right, depth + 1, pos * 2 + 1)

        dfs(root, 0, 0)
        return self.ans
