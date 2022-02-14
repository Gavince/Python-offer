# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 下午3:55
# @Author  : gavin
# @FileName: 124.编辑距离.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述:
	给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符
解题方法:
动态规划
1.状态定义，dp[i][j]表示word1[:i]到word2[:j]的最小编辑距离
2.起始状态，dp[0][i] = 0, dp[j][0] = 0表示空字符编辑
3.状态转移
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
4.返回值，dp[m][n]

时间复杂度：O(m*n)
空间复杂度：O(m*n)

原题链接：https://leetcode-cn.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        if n * m == 0:
            return m + n

        # 状态定义
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 起始状态
        # 第一列
        for i in range(m + 1):
            dp[i][0] = i
        # 第一行
        for j in range(n + 1):
            dp[0][j] = j
        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        # 返回值
        return dp[m][n]