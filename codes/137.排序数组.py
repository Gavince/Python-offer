# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 上午8:15
# @Author  : gavin
# @FileName: 137.排序数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 nums，请你将该数组升序排列。

解题思路：
快速排序（比较点的选择增加随机性）和归并排序
"""
import random
from typing import List


class Solution:
    # 随机快速排序
    def sortArray(self, nums: List[int]) -> List[int]:

        def quickSort(nums, strat, end):
            if strat >= end:
                return
            i, j = strat, end
            # 随机选择起始比较点
            index = random.randint(i, j)
            nums[i], nums[index] = nums[index], nums[i]
            pivot = nums[i]
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] < pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            quickSort(nums, strat, i - 1)
            quickSort(nums, i + 1, end)

        quickSort(nums, 0, len(nums) - 1)
        return nums

    # 归并排序
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        # 拆分
        return self.merge(self.sortArray(left), self.sortArray(right))

    def merge(self, left, right):

        result = []

        # 公共部分比较合并
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 剩余部分合并
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))

        return result