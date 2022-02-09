# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 上午10:06
# @Author  : gavin
# @FileName: 84.不同的二叉搜索树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
问题描述
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
返回满足题意的二叉搜索树的种数。

解题方法：
动态规划(四步走原则)
(1)定义转态：dp[i]表示连续的i个数，所有可能的BST组合个数；
(2)状态转移：dp[i] += dp[j]*dp[i - j - 1]  2 <= i <= n, 2 <=  j <=  i - 1；
eg: dp[2] = dp[1] * dp[0] + dp[0] * dp[1]
(3)初始状态：dp[0] = 1, dp[1] = 1 表示无节点和只有一个结点时, BST个数为1 ；
(4)返回值：dp[n]连续n个结点的BST组合个数。
时间复杂度：O(N^2)
空间复杂度：O(N)
"""


class Solution:

    def numTrees(self, n: int) -> int:
        # 定义转态
        dp = [0] * (n + 1)
        # 初始状态
        dp[0], dp[1] = 1, 1
        # 状态转移
        for i in range(2, n + 1):
            # 将 i - 1 个数左右对分
            # 左：j 右：i - j - 1
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        # 返回值
        return dp[n]
