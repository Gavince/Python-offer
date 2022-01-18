# -*- coding: utf-8 -*-
# @Time    : 2021/10/3 下午5:45
# @Author  : gavin
# @FileName: 153.最长重复子数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

解题思路：
动态规划
dp[i][j]代表以A[i-1]与B[j-1]结尾的公共字串的长度,公共字串必须以A[i-1]，B[j-1]结束，
即当A[i-1] == B[j-1]时，dp[i][j] = dp[i-1][j-1] + 1; 当A[i-1] != B[j-1]时，
以A[i-1]和B[j-1]结尾的公共字串长度为0,dp[i][j] = 0。输出最大的公共字串的长度即为最
长重复字串。
时间复杂度：O(M*N)
空间复杂度：O(M*N)
注意：
记住，子序列默认不连续，子数组默认连续
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        m, n = len(nums1), len(nums2)

        # 定义状态和起始值
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        ans = 0

        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans