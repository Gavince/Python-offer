# -*- coding: utf-8 -*-
# @Time    : 2021/12/9 下午4:46
# @Author  : gavin
# @FileName: 170.完全平方数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。你
需要让组成和的完全平方数的个数最少。给你一个整数 n ，返回和为 n 的完全平方数的最少数量
。完全平方数是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

解题方法：
动态规划
1.定义dp：dp[i]表示构成正整数i的最小平方个数
2.初始值：dp[0] = 0
3.转态转移：dp[i] = min(dp[i - j*j] + 1, dp[i])
4.返回值：最小平方个数
时间复杂度：O(N*sqrt(N))
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/perfect-squares/
"""


class Solution:
    def numSquares(self, n: int) -> int:

        # 定义dp
        dp = list(range(n + 1))
        # 状态转移
        for i in range(1, n + 1):
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i - j * j] + 1, dp[i])
                j += 1
        # 返回值
        return dp[n]
