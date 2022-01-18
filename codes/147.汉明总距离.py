# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 上午8:08
# @Author  : gavin
# @FileName: 147.汉明总距离.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
    两个整数汉明距离 指的是这两个数字的二进制数对应位不同的数量。给你一个
整数数组 nums，请你计算并返回 nums 中任意两个数之间汉明距离的总和。

解题方法：
位操作算法
"""

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(30):
            c = sum([((val >> i) & 1) for val in nums])
            ans += c * (n - c)

        return ans
