# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 上午10:52
# @Author  : gavin
# @FileName: 112.数组中的第K个最大元素.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
题目描述：
    给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。请注意，
你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

解题方法：
快速排序
时间复杂度：O(NlogN)
空间复杂度：O(1)
"""

import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSort(start, end):

            if start >= end:
                return

                # 寻找哨兵结点
            low, high = start, end
            index = random.randint(low, high)
            nums[low], nums[index] = nums[index], nums[low]
            pivot = nums[low]

            # 划分区间
            while low < high:
                while low < high and pivot <= nums[high]:
                    high -= 1
                nums[low] = nums[high]
                while low < high and pivot > nums[low]:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            if low > len(nums) - k:
                quickSort(start, low - 1)
            else:
                quickSort(low + 1, end)

        quickSort(0, len(nums) - 1)

        return nums[-k]