# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 下午7:58
# @Author  : gavin
# @FileName: 156.最长连续递增序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，
都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ...,
nums[r - 1], nums[r]] 就是连续递增子序列。
实例：
1 2 5 8 6 3 4 5 6

解题方法：
双指针 + 滑动窗口
时间复杂度：O(N)
空间复杂度：O(1)
"""


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        if not nums: return 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            if right > 0 and nums[right] <= nums[right - 1]:
                left = right
            ans = max(ans, right - left + 1)

        return ans