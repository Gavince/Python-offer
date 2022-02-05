# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 下午3:12
# @Author  : gavin
# @FileName: 154.不同路径II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    一个机器人位于一个 m x n 网格的左上角（起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为
“Finish”）。现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路
径？网格中的障碍物和空位置分别用1和0来表示。

解题方法：
动态规划
(1) 定义状态：dp[i][j]表示到达i, j的不同路径
(2) 初始值：dp[0][j] = 1, dp[i][0] = 1，遇见障碍 break
(3) 转态转移：　dp[i][j] = dp[i][j - 1] + dp[i - 1][j]，遇见障碍 continue
(4) 返回值：dp[-1][-1]
时间复杂度：O(n*m)
空间复杂度：O(m*n)

原题链接：https://leetcode-cn.com/problems/unique-paths-ii/
"""


class Solution:


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # 定义dp
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        # 定义初始转态
        # 有障碍区进行跳转
        for i in range(m):
            if obstacleGrid[i][0]: break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j]: break
            dp[0][j] = 1

        # 转态转移
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]: continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 返回值
        return dp[m - 1][n - 1]
