# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 上午10:48
# @Author  : gavin
# @FileName: 169.最大正方形.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
示例:
输入：matrix = [["1","0","1","0","0"]
            ,["1","0","1","1","1"]
            ,["1","1","1","1","1"]
            ,["1","0","0","1","0"]]
输出：4

解题方法：
动态规划
1.定义dp：dp[i][j]表示以i,j为右下角的最大正方形
2.初始值：
3.转态转移：dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
4.返回值：最大面积
时间复杂度：O(MN)
空间复杂度：O(MN)

原题链接：https://leetcode-cn.com/problems/maximal-square/
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m, n = len(matrix), len(matrix[0])
        # 如果只有一列或者一行， 则不可能构成正方形
        if m == 0 or n == 0:
            return 0
        # 定义dp
        dp = [[0] * n for _ in range(m)]
        max_slide = 0

        # 转态转移
        for i in range(m):
            for j in range(n):
                # 边界条件， dp[i][j]表示以i,j为右下角的最大正方形
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_slide = max(max_slide, dp[i][j])

        # 返回值
        return max_slide * max_slide
