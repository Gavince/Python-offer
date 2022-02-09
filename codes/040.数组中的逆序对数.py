# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 上午9:03
# @Author  : gavin
# @FileName: 40.数组中的逆序对数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，
求出这个数组中的逆序对的总数。

"""


class Solution:
    def __init__(self):
        self.cnt = 0

    def reversePairs(self, nums: List[int]) -> int:

        self.mergeSort(nums)
        return self.cnt

    def mergeSort(self, nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        # 拆分

        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):

        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                self.cnt += (len(left) - i)

        result += left[i:]
        result += right[j:]

        return result