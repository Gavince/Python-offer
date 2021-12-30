# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 上午9:21
# @Author  : gavin
# @FileName: 129.零钱兑换.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。计算并
返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。你可
以认为每种硬币的数量是无限的。

解题方法：
动态规化
1.状态定义：dp[i]表示组成和为i的零钱个数
2.起始状态：dp[0]表示为零
3.状态转移：dp[i] = min(dp[i], dp[i - coin] + 1)
4.返回值: dp[-1]
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # 定义状态并赋予初值
        dp = [0] + [10001] * amount
        # 状态转移
        for i in range(1, amount + 1):
            for coin in coins:
                diff = i - coin
                if diff >= 0:
                    # dp[7] = min(dp[7 - 1], dp[7 - 5], dp[7 - 2]) + 1
                    dp[i] = min(dp[i], dp[diff] + 1)
        # 返回值
        return dp[-1] if dp[-1] != 10001 else -1
