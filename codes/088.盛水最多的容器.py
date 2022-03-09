# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 上午9:14
# @Author  : gavin
# @FileName: 88.盛水最多的容器.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在
坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。找出其中的
两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。

解题方法：
(1)暴力法
枚举所有可能的最大最大盛水体积
时间复杂度:O(N^2)
空间复杂度:O(1)

(2)双指针法
原则：容器的最大面积是由短板决定的，固定长板，移动短板
时间复杂度:O(N)
空间复杂度:O(1)

双指针移动的合理性：
    其实无论是移动短指针和长指针都是一种可行求解。 只是，一开始就已经把指针定
义在两端，如果短指针不动，而把长指针向着另一端移动，两者的距离已经变小了，无论
会不会遇到更高的指针，结果都只是以短的指针来进行计算。 故移动长指针是无意义的。

原题链接：https://leetcode-cn.com/problems/container-with-most-water/
"""
from typing import List


class Solution:

    def maxArea1(self, height) -> int:
        """暴力法"""
        # 双重遍历
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if height[i] < height[j]:
                    max_area = max(max_area, height[i] * (j - i))
                else:
                    max_area = max(max_area, height[j] * (j - i))
        return max_area

    def maxArea2(self, height: List[int]) -> int:

        i, j, max_area = 0, len(height) - 1, 0
        # i < j 表示坐标轴无重叠
        while i < j:
            # 移动长边无意义
            if height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1

        return max_area
