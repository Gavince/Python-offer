# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 上午9:54
# @Author  : gavin
# @FileName: 160.区间合并.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

解题方法：
排序合并

原题链接：https://leetcode-cn.com/problems/merge-intervals/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # 判断区间的连续性
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged