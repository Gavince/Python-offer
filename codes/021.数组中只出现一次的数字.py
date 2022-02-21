# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 上午8:08
# @Author  : gavin
# @FileName: 21.数组中只出现一次的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述:
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

解题方法:
1.字典
2.异或
概念：参与运算的两个值，如果两个相应位相同，则结果为0，否则为1。即：0^0=0， 1^0=1，
0^1=1， 1^1=0

时间复杂度：O(N)
空间复杂度：O(1)
原题链接：https://leetcode-cn.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a
