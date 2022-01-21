# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 上午10:58
# @Author  : gavin
# @FileName: 198.最大矩形.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包
含 1 的最大矩形，并返回其面积。

解题方法：
每一程构建直方图，通过使用直方图最大矩形面积来获取最大矩形操作
单调栈
时间复杂度：O(MM)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/maximal-rectangle/
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        max_rect = 0
        heights = [0]*(n + 1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            # 单调栈计算最大矩形面积
            stack = [-1]
            for right, num in enumerate(heights):
                while stack and heights[stack[-1]] > num:
                    index = stack.pop()
                    max_rect = max(max_rect, heights[index]*(right - stack[-1] -1))
                stack.append(right)

        return max_rect