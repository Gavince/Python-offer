# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 下午2:32
# @Author  : gavin
# @FileName: 122.最长公共子序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	给定两个字符串text1 和text2，返回这两个字符串的最长公共子序列的长度。如果不存在
公共子序列 ，返回0 。一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字
符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。例如，"ace"
是 "abcde" 的子序列，但 "aec" 不是 "abcde"的子序列。两个字符串的公共子序列是这两个
字符串所共同拥有的子序列。

解题方法：

动态规划
1.状态定义，dp[i][j]表示text1[:i]和text2[:j]最长的公共子序列
2.起始状态，dp[0][i] = 0, dp[j][0] = 0表示空字符和任何字符串的公共子序列长度为0
3.状态转移

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

4.返回值，dp[m][n]

时间复杂度：O(m*n)
空间复杂度：O(m*n)

原题链接：
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        # 状态定义和起始值
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]