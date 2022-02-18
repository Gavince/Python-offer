# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 下午8:40
# @Author  : gavin
# @FileName: 109.接雨水.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
下雨之后能接多少雨水。

示例：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，
在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

解题方法：
(1）暴力法
遍历每一个下标的左右区间，寻找可能的凹槽
时间复杂度：O(N^2)
空间复杂度：O(1)

(2)双指针
使用left和right指针，遍历所有节点
时间复杂度：O(N)
空间复杂度：O(1)

原题链接:https://leetcode-cn.com/problems/trapping-rain-water/
"""
from typing import List


class Sulution:

    def trap0(self, height: List[int]) -> int:
        """接雨水（暴力法）"""

        ans = 0
        # 遍历下标
        for i in range(len(height)):
            max_left, max_right = 0, 0
            for j in range(0, i):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            # 盛雨水
            if min(max_left, max_right) > height[i]:
                ans += min(max_left, max_right) - height[i]

        return ans

    def trap1(self, height:List[int]) -> int:
        """双指针法"""

        if not height: return 0
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        max_left, max_right = height[0], height[n - 1]

        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1

        return ans
