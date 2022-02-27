# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 上午8:13
# @Author  : gavin
# @FileName: 56.扑克牌中的顺子.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身
，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

解题方法：
# 条件（大小王除外, 且不重复）
max - min < 5

注意：
1. 不是一副扑克牌，大小王不止一张，即也有可能抽到五张大小，组成任意的
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
"""


class Solution:

    def isSraight(self, nums: List[int]) -> bool:

        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue  # 遇见大小王则跳过
            mi = min(mi, num)
            ma = max(ma, num)
            if num in repeat: return False  # 有重复数值,直接返回
            repeat.add(num)

        return abs(ma - mi) < 5

    def isStraight(self, nums: List[int]) -> bool:

        # 先排序后计算
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1  # 遍历有零部分
            elif nums[i] == nums[i + 1]:
                return False  # 非零部分存在重复，不满足条件
        return nums[4] - nums[joker] < 5
