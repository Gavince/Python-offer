# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 上午8:33
# @Author  : gavin
# @FileName: 146.寻找两个正序数组的中位数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请
你找出并返回这两个正序数组的 中位数 。

解题方法：
归并排序的归并阶段
时间复杂度：O(m + n)
空间复杂度：O(m + n)

原题链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = self.merge(nums1, nums2)
        # 奇数
        mid = len(res) // 2
        if len(res) % 2:
            return res[mid]
        else:
            return (res[mid - 1] + res[mid]) / 2

    def merge(self, arr1, arr2):

        result = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result += arr1[i:]
        result += arr2[j:]

        return result