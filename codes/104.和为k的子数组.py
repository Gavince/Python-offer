# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 上午8:20
# @Author  : gavin
# @FileName: 104.和为k的子数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组
的个数。

示例：
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

解题方法：
(1)暴力法
时间复杂度：O(N^2)
空间复杂度：O(1)
(2)前缀表达式
pre_A + k = pre_B
时间复杂度：O(N)
空间复杂度：O(N)
"""
from collections import defaultdict


class Solution:

    def subarraySum1(self, nums, k):
        """暴力法"""
        count = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, -1, -1):
                sum += nums[end]
                if sum == k:
                    count += 1

        return count

    def subarraySum2(self, nums, k):
        """前缀和表达"""

        # 统计当前前缀和
        nums_times = defaultdict(int)
        nums_times[0] = 1
        cur_sums = 0
        count = 0

        for i in range(len(nums)):
            cur_sums += nums[i]
            if cur_sums - k in nums_times:
                count += nums_times[cur_sums - k]
            nums_times[cur_sums] += 1

        return count
