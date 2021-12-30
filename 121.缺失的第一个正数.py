# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 下午9:57
# @Author  : gavin
# @FileName: 121.缺失的第一个正数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""

问题描述：
    给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

解题方法：
时间复杂度:O(N)
空间复杂度:O(1)

"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        # 1. 标记非正数
        # 1 -2 -5 5 6
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        # 2. index标记
        for i in range(n):
            # 3 4 -1 1
            index = abs(nums[i])
            if index <= n:
                nums[index - 1] = -abs(nums[index - 1])

        # 3. 找出第一个正数
        # 1 3 4 5
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # 1 2 3 4
        return n + 1