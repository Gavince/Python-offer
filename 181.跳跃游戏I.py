# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 上午10:22
# @Author  : gavin
# @FileName: 181.跳跃游戏I.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。数组中的每个元素代
表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个下标。

解题方法：
贪心枚举
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n, right_most = len(nums), 0

        # 贪心遍历
        for i in range(n):
            # 在可跳越范围内继续起跳
            if i <= right_most:
                # 更新最远起跳位置
                right_most = max(right_most, nums[i] + i)
                # 是否可到达
                if right_most >= n - 1:
                    return True

        return False