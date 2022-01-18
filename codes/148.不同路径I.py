# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 上午9:53
# @Author  : gavin
# @FileName: 148.不同路径I.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。机器人每
次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

解题方法：
动态规划
(1) 定义状态：dp[i][j]表示到达i, j的不同路径
(2) 初始值：dp[0][j] = 1, dp[i][0] = 1
(3) 转态转移：dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
(4) 返回值：dp[-1][-1]
时间复杂度：O(n*m)
空间复杂度：O(m*n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # 定义转态
        dp = [[0] * n for _ in range(m)]
        # 初始转态
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 转态转移
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回值
        return dp[-1][-1]
