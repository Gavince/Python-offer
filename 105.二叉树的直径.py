# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 上午9:33
# @Author  : gavin
# @FileName: 105.二叉树的直径.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点
路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

实例：
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]

解题方法：
深度优先遍历
时间复杂度：O(N)
空间复杂度：O(height)
"""


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root):
            if root is None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            cur_high = 1 + left + right
            self.ans = max(self.ans, cur_high)

            return max(left, right) + 1

        dfs(root)

        return self.ans - 1