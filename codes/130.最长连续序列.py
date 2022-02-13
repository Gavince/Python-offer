# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 下午5:36
# @Author  : gavin
# @FileName: 130.最长连续序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原
数组中连续）的长度。请你设计并实现时间复杂度为O(n) 的算法解决此问题。

解题方法：
哈希表
注意不要求序列元素在数组中连续

时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_streak = 0
        num_sets = set(nums)

        # 遍历
        for num in num_sets:
            # 无前驱才能作为起始结点
            if num - 1 not in num_sets:
                cur_num = num
                cur_streak = 1
                # 是否有后继结点
                while cur_num + 1 in num_sets:
                    cur_num += 1
                    cur_streak += 1
                longest_streak = max(longest_streak, cur_streak)

        return longest_streak