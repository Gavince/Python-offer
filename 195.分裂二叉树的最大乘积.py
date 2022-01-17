# -*- coding: utf-8 -*-
# @Time    : 2022/1/16 上午9:28
# @Author  : gavin
# @FileName: 195.分裂二叉树的最大乘积.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一棵二叉树，它的根为root 。请你删除 1 条边，使二叉树分裂
成两棵子树，且它们子树和的乘积尽可能大。由于答案可能会很大，请你将
结果对 10^9 + 7 取模后再返回。

解题方法：
DFS
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree/
"""


class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        # 记录各个结点的node_sum
        list_sum = []

        def dfs(root):
            if root is None: return 0
            cur_node_sum = dfs(root.left) + dfs(root.right) + root.val
            list_sum.append(cur_node_sum)

            return cur_node_sum

        total_sum = dfs(root)
        ans = float("-inf")
        for sum_ in list_sum:
            ans = max(ans, sum_ * (total_sum - sum_))

        return ans % (10 ** 9 + 7)