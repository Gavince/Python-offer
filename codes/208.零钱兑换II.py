# -*- coding: utf-8 -*-
# @Time    : 2022/4/23 上午8:42
# @Author  : gavin
# @FileName: 208.零钱兑换II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示
总金额。请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出
总金额，返回 0 。假设每一种面额的硬币有无限个。题目数据保证结果符合 32 位带
符号整数。

解题方法：
背包问题
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/coin-change-2/
图示两种不同遍历顺序：https://leetcode-cn.com/problems/coin-change-2/solution/c-bei-bao-wen-ti-by-yizhe-shi/
"""

from typing import List


class Solution:
    def changeforCoins(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        # 初始化dp
        dp[0] = 1
        for coin in coins:
            print("coin", coin)
            for j in range(coin, amount + 1):
                print("j", dp[j - coin])
                dp[j] += dp[j - coin]
                print("dp{}".format(j), dp[j])
        return dp[amount]

    def changeforAmount(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        # 初始化dp
        dp[0] = 1

        for j in range(0, amount + 1):
            for coin in coins:
                if j - coin > 0:
                    print("coin", coin)
                    dp[j] += dp[j - coin]
        return dp[amount]


if __name__ == "__main__":
    obj = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(obj.changeforCoins(amount, coins))
    print(obj.changeforAmount(amount, coins))
