# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 上午9:24
# @Author  : gavin
# @FileName: 74.数组中数字出现的次数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
数组中数字出现的次数I
问题描述：
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要
求时间复杂度是O(n)，空间复杂度是O(1)。

实例：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

解题方法:

数组中数字出现的次数II：
问题描述：

实例：

解题方法：

"""


class Solution:

    def singleNumber(self, nums):

        x, y, n, m = 0, 0, 0, 1
        # 遍历寻找X^y
        for num in nums:
            n ^= num
        # 寻找首尾不为一的位置
        while n & m == 0:
            m << 1

        # 划分自组并遍历
        for num in nums:
            if num & m: x ^= num
            else: y ^= num

        return x, y