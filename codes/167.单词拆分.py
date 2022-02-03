# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 上午10:56
# @Author  : gavin
# @FileName: 167.单词拆分.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个字符串 s 和一个字符串列表 wordDict 作为字典，判定s 是否可以由空
格拆分为一个或多个在字典中出现的单词。说明：拆分时可以重复使用字典中的单词。

示例：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"

解题方法：
动态规划
时间复杂度：O(N^2)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/word-break/
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 定义dp
        n = len(s)
        dp = [False]*(n + 1)
        # 赋予初值
        dp[0] = [True]
        # 转态转移
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    #　下一个状态的起始点标识
                    dp[j] = True
        # 返回值
        return dp[n]
