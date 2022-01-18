# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 下午3:38
# @Author  : gavin
# @FileName: 77.两数之和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值
的那两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，
数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。

解题方法：
方法一：暴力求解
时间复杂度O(N^2)
空间复杂度O(1)

方法二：哈希表(空间换时间)
时间复杂度:O(N)
空间复杂度:O(N)

注意：
同一个元素不能重复出现
[4, 4, 2, 1, 2]   target = 4
不能出现[2, 2] or [4, 4] 应该出现[2, 4]的索引组合
"""
from typing import List


class Solution:

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """暴力求解"""

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """哈希表"""

        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            # {values: index}
            hashtable[nums[i]] = i

        return []