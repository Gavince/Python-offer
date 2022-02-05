# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 下午7:27
# @Author  : gavin
# @FileName: 157.和为s的两个数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有
多对数字的和等于s，则输出任意一对即可。

解题方法：
主要突破点在于“递增排序”
双指针，对撞双指针
时间复杂度：(N)
空间复杂度:O(1)

原题链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]

        return []