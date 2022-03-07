# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 上午9:24
# @Author  : gavin
# @FileName: 65.股票的最大利润I.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次
可能获得的最大利润是多少？

示例：
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候
卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

解题方法：
(1)暴力法
时间复杂度:O(N^2)
空间复杂度:O(1)

(2)一次遍历
优化动态规划，不保留中间状态的值
时间复杂度:O(N)
空间复杂度:O(1)

(3)动态规划
1.定义转态：dp[i] 到时间结点i的最大利润
2.初始化转态：dp = [0]*n
3.状态转移：dp[i] = max(dp[i - 1], prices[i] - min_cost)
4.返回值:dp[-1]
时间复杂度:O(N)
空间复杂度:O(N)

原题链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """暴力法"""

        profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, prices[j] - prices[i])

        return profit

    def maxProfit(self, prices) -> int:
        """一次遍历"""

        cost, profit = float("+inf"), 0
        for price in prices:
            # 低谷
            cost = min(cost, price)
            # 利润最大化
            profit = max(profit, price - cost)

        return profit

    def maxProfit(self, prices) -> int:
        """动态规划"""

        n = len(prices)
        if n == 0:
            return 0
        # 定义dp和初始状态
        dp = [0] * n
        min_cost = prices[0]
        for i in range(1, n):
            min_cost = min(min_cost, prices[i])
            # 状态转移
            dp[i] = max(dp[i - 1], prices[i] - min_cost)
        # 返回值
        return dp[-1]
