# -*- coding: utf-8 -*-
# @Time    : 2021/2/14 上午10:21
# @Author  : gavin
# @FileName: 36.连续子数组的最大和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个
元素），返回其最大和。

解题方法：
动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 ans
如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果

动态规划:
时间复杂度：O(N)
空间复杂度：O(N)

优化的动态规划:
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/maximum-subarray/
"""


class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        """动态规划"""

        if not nums: return 0
        # 定义状态
        dp = [0]*len(nums)
        # 初始值
        dp[0] = nums[0]
        # 状态转移
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        # 返回值
        return max(dp)

    def MaxArray(self, nums):
        """优化的动态规划"""

        if not nums: return 0
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)

        return max(nums)
