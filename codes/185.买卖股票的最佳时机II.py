# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 上午10:59
# @Author  : gavin
# @FileName: 185.买卖股票的最佳时机II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个数组 prices ，其中prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多
次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

解题方法：
突破点：只要今天比昨天大，就卖出。
解释：[7, 1, 5, 6] 第二天买入，第四天卖出，收益最大（6-1），所以一般人可能会想，
怎么判断不是第三天就卖出了呢? 这里就把问题复杂化了，根据题目的意思，当天卖出以后，
当天还可以买入，所以其实可以第三天卖出，第三天买入，第四天又卖出（（5-1）+ （6-5）
 === 6 - 1）。所以算法可以直接简化为只要今天比昨天大，就卖出。

连续正向收益下：prices[n] - prices[1] = (prices[n] - prices[n - 1]) + ....(prices[2] - princes[1])
负向收益不累计：prices[i] - prices[j] < 0
时间复杂度：O(n)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:  # 统计正向收益
                profit += tmp

        return profit