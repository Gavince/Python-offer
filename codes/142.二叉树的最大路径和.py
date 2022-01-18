# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 上午8:48
# @Author  : gavin
# @FileName: 142.二叉树的最大路径和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点
在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。路径和是路径中
各节点值的总和。给你一个二叉树的根节点 root，返回其 最大路径和 。

解题方法：
DFS
1.
 /
/
2.
\
 \
3.
-
4.
  -
 / \
/   \
"""


class Solution:

    def __init__(self):
        self.max_gain = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(root):
            if root is None:
                return 0
            # 计算左右结点收益
            left_gain = max(dfs(root.left), 0)
            right_gain = max(dfs(root.right), 0)
            # 更新当前结点的收益
            cur_gain = root.val + left_gain + right_gain
            self.max_gain = max(cur_gain, self.max_gain)
            # 只返回左右子树中的任意一个，保证路径的唯一性
            return root.val + max(left_gain, right_gain)

        dfs(root)

        return self.max_gain


