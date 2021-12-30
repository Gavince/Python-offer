# -*- coding: utf-8 -*-
# @Time    : 2021/8/14 上午8:48
# @Author  : gavin
# @FileName: 135.长度最小的子数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个含有n个正整数的数组和一个正整数 target 。找出该数组中满足其和 ≥ target
的长度最小的连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
如果不存在符合条件的子数组，返回 0 。

解题方法：
(1)暴力法
时间复杂度：O(N*N)
空间复杂度：O(1)

(2)双指针法
注意以下情况的返回值
nums: [1, 1, 1, 1, 1, 1, 1, 1]
target: 11
ans: 0
时间复杂度：O(N)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    # 暴力法
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0
        ans = len(nums) + 1
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    ans = min(ans, j - i + 1)
        return ans
    # 双指针法
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums:
            return 0

        left, right = 0, 0
        n = len(nums)
        ans = n + 1
        total = 0

        while right < n:
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1

        return 0 if ans == n + 1 else ans
