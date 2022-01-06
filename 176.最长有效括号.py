# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 上午10:13
# @Author  : gavin
# @FileName: 176.最长有效括号.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

解题方法：
动态规划
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
相似题目：有效的括号、括号生成
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        # 定义dp
        dp = [0] * n  # 到第i位置的最大括号
        res = 0
        # 转态转移
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    # "()()()"
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    # "()(())"
                    if i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

                res = max(dp[i], res)
        # 返回值
        return res
