# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 上午10:06
# @Author  : gavin
# @FileName: 182.跳跃游戏II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给你一个非负整数数组nums ，你最初位于数组的第一个位置。数组中的每个元素代
表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个
位置。假设你总是可以到达数组的最后一个位置。

解题方法：
动态规划
nums = [2,3,1,1,4]
寻找在当前起跳范围内的最大起跳长度
max_pos: 2, 4
step:    1, 2

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/jump-game-ii/
"""


class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            if max_pos >= i:
                # 寻找最大起跳点
                max_pos = max(max_pos, nums[i] + i)
                if end == i:
                    step += 1
                    end = max_pos
        return step