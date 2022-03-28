# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 上午9:54
# @Author  : gavin
# @FileName: 196.矩阵中的最长递增路径.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个m x n 整数矩阵matrix ，找出其中最长递增路径的长度。
对于每个单元格，你可以往上，下，左，右四个方向移动。你能在对角线方
向上移动或移动到边界外（即不允许环绕）。

解题方法：
深度优先遍历+记忆化优化
思路：朴素深度优先搜索的时间复杂度过高的原因是进行了大量的重复计算，同一个单
元格会被访问多次，每次访问都要重新计算。由于同一个单元格对应的最长递增路径的
长度是固定不变的，因此可以使用记忆化的方法进行优化。用矩阵 memo 作为缓存矩
阵，已经计算过的单元格的结果存储到缓存矩阵中。

时间复杂度：O(MN)
空间复杂度：O(MN)

原题链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dis = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # 记忆化
        memo = [[0] * n for _ in range(m)]
        # 遍历所有可能的结点，寻找最长路径
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, i, j, dis, memo))
        return ans

    def dfs(self, matrix, i, j, dis, memo):

        if memo[i][j] != 0: return memo[i][j]
        longest_dis = 1
        for di, dj in dis:
            x, y = i + di, j + dj
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[i][j] < matrix[x][y]:
                longest_dis = max(longest_dis, self.dfs(matrix, x, y, dis, memo) + 1)

        # 记忆当前结点的最长路径值
        memo[i][j] = longest_dis

        return longest_dis
