# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 上午8:35
# @Author  : gavin
# @FileName: 63.礼物的最大值.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右
下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

实例：
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

注意：
(1)入口为左上角,出口为右下角
(2)每次向下或向右移动一格

解题方法：
动态规划
"""


class Solution:

    def maxValue(self, grid) -> int:
        """礼物的最大值"""
        m, n = len(grid), len(grid[0])
        # 初始化第一行
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        # 初始化第一列
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # 遍历i,j结点
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])

        # 右下角的值
        return grid[-1][-1]
