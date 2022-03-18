# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 上午10:11
# @Author  : gavin
# @FileName: 155.搜索旋转排序数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    整数数组 nums 按升序排列，数组中的值互不相同 。在传递给函数之前，nums 在预先未知的某个下标
k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1],
nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标
3 处经旋转后可能变为[4,5,6,7,0,1,2] 。给你旋转后的数组 nums 和一个整数 target ，如果
nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。

注意:整数数组nums按升序排列，数组中的值互不相同,且之旋转一次

解题方法：
使用二分法,通过寻找旋转中心点,以在部分有序数组中寻找目标值
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4

时间复杂度：O(logN)
空间复杂度：O(1)

原题链接:https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums: return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 1 2 3 4 5
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 4 5 1 2 3
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1