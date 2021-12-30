# -*- coding: utf-8 -*-
# @Time    : 2021/5/5 上午8:34
# @Author  : gavin
# @FileName: 67.n个骰子的点数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i
小的那个的概率。

实例：
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

解题方法：
动态规划
dp[i - 1]的骰子对d[i + K]的的贡献度

注意：
输出结果（概率值）从小到大排序
"""


class Solution:

    def dicesProbability(self, n: int):
        """投掷骰子"""

        # 初始化dp
        dp = [1.0/6.0] * 6
        for i in range(2, n + 1):
            # 点数和的数量
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6

            dp = tmp
        return dp