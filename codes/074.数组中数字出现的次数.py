# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 上午9:24
# @Author  : gavin
# @FileName: 74.数组中数字出现的次数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
数组中数字出现的次数I
问题描述：
    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个
只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

实例：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

解题方法:
位运算

时间复杂度：O(n)
空间复杂度：O(1)
原题链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/

进阶题目：数组中数字出现的次数II
问题描述：
    在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只
出现一次的数字。

示例：
输入：nums = [3,4,3,3]
输出：4

解题方法：
位运算

时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
"""


class Solution:

    def singleNumberfor1(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a

    def singleNumberfor2(self, nums: List[int]) -> List[int, int]:

        x, y, n, m = 0, 0, 0, 1
        # 遍历寻找X^y
        for num in nums:
            n ^= num
        # 寻找首尾不为一的位置
        while n & m == 0:
            m <<= 1

        # 划分自组并遍历
        for num in nums:
            if num & m: x ^= num
            else: y ^= num

        return x, y

    def singleNumberfor3(self, nums: List[int]) -> int:

        res = 0
        for i in range(32):
            cnt = sum([((num >> i) & 1) for num in nums])
            if cnt % 3:
                if i == 31:
                    res -= 1 << i
                else:
                    res |= 1 << i
        return res