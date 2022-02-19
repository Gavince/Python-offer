# -*- coding: utf-8 -*-
# @Time    : 2022/2/19 上午9:17
# @Author  : gavin
# @FileName: 204.汉明总距离.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
    两个整数的汉明距离 指的是这两个数字的二进制数对应位不同的数量。给你一个整
数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。

示例：
输入：nums = [4,14,2]
输出：6
解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6

解题方法：
4: 0100
14:1110
2: 0010
-------
统计每一位置上1的个数
(vall>>i)&1
2*1 + 1*2 + 2*1 = 6
时间复杂度：O(n*L)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/total-hamming-distance/
"""


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        ans, n = 0, len(nums)
        for i in range(30):
            c = sum([(val >> i) & 1 for val in nums])
            ans += c * (n - c)

        return ans