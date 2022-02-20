# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 下午2:14
# @Author  : gavin
# @FileName: 81.最长回文子串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个字符串 s，找到 s 中最长的回文子串。

字符串的回文：
	对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的
两个字母去除之后，它仍然是个回文串。例如对于字符串“ababa”，如果我们
已经知道“bab” 是回文串，那么 “ababa” 一定是回文串，这是因为它的首
尾两个字母都是a”。

示例：
遍历不同长度下的不同起始位置
"eabcbaf"
最长回文子串: "abcba"
长度： 5

解题方法：
动态规划
(1)状态定义：d[i][j]表示s[i:j]为回文子串；
(2)状态转移：d[i][j] = dp[i + 1][j - 1]，子问题是否为回文子串；
(3)初始状态：dp[i][i] = True 表示只有一个字符时为回文子串；
(4)返回值：最长的回文子串长度。

时间复杂度O(n^2)
空间复杂度O(n^2)

原题链接：https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


class Solution:

    def longestPalindrom(self, s: str) -> str:

        n = len(s)
        if n < 2:
            return s
        max_len, begin = 1, 0
        # 定义状态
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        # 遍历不同长度的回文子串
        for L in range(2, n + 1):
            # 指定左边界，并根据长度确定右边界
            for i in range(n):
                # i 为左起始点， j 为右起始点
                j = i + L - 1
                # 超出右边界
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 更新最长回文字符长度
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin: begin + max_len]
