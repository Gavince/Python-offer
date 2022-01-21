# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 上午10:41
# @Author  : gavin
# @FileName: 197.直方图最大矩形面积.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定非负整数数组 heights，数组中的数字用来表示柱状图中各个柱子
的高度。每个柱子彼此相邻，且宽度为 1 。求在该柱状图中，能够勾勒出来
的矩形的最大面积。

解题方法：
单调栈计算
时间复杂度：O(N)
空间复杂度：O(N)

相似题型（柱状图中最大的矩形）：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
原题链接：https://leetcode-cn.com/problems/0ynMMM/
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if not heights: return 0
        max_area = 0
        heights.append(0)
        # 使用单调栈，存储连续递增的高度，并增加哨兵
        stack = [-1]
        for right, num in enumerate(heights):
            while stack and heights[stack[-1]] > num:
                cur_index = stack.pop()
                max_area = max(max_area, heights[cur_index]*(right - stack[-1] - 1))
            stack.append(right)

        return max_area