# -*- coding: utf-8 -*-
# @Time    : 2021/10/16 上午8:37
# @Author  : gavin
# @FileName: 159.在排序数组中查找元素的第一个和最后一个位置.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开
始位置和结束位置。如果数组中不存在目标值 target，返回[-1, -1]。

解题方法：
二分法
时间复杂度：O(logN)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if target not in nums: return [-1, -1]

        def helper(tar):

            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if tar >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        return [helper(target - 1), helper(target) - 1]
