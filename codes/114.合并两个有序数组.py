# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 下午8:39
# @Author  : gavin
# @FileName: 114.合并两个有序数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1
成为一个有序数组。初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1
的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。

解题方法：
逆向双指针
特殊情况:当num1数组为零时，即[0] 0 [1] 1，需要执行nums1[:] = nums2[:]

时间复杂度：O(m + n)
空间复杂度:O(1)

原题连接：https://leetcode-cn.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[tail] = nums1[m - 1]
                m -= 1
            else:
                nums1[tail] = nums2[n - 1]
                n -= 1
            tail -= 1
        nums1[:n] = nums2[:n]
