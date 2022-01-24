# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 下午7:38
# @Author  : gavin
# @FileName: 175.最短无序连续子数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个
子数组进行升序排序，那么整个数组都会变为升序排序。请你找出符合题意的
最短子数组，并输出它的长度。

解题方法：
左右双指针:从左到右循环，记录最大值为 max，若 nums[i] < max, 则
表明位置 i 需要调整, 循环结束，记录需要调整的最大位置 i 为 high;
同理，从右到左循环，记录最小值为 min, 若 nums[i] > min, 则表
明位置 i 需要调整，循环结束，记录需要调整的最小位置 i 为 low.

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float(inf), -1
        for i in range(n):
            # 右面不能存在比nums[right]小的值
            if nums[i] < maxn:
                right = i
            else:
                maxn = nums[i]
            # 左面不能存在比nums[left]大的值
            if nums[n - i -1] > minn:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1