# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 上午8:49
# @Author  : gavin
# @FileName: 131.第N位数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第
n 位数字。注意：n 是正数且在 32 位整数范围内（n < 231）。

解题方法：
时间复杂度：O(N)
空间复杂度：O(1)
"""


class Solution:
    def findNthDigit(self, n: int) -> int:

        n -= 1
        # 遍历可能的位数
        for digit in range(1, 11):
            firsr_num = 10**(digit - 1)
            # 判断查找数字位于第几位数
            if n < 9*digit*firsr_num:
                # 第几位数的第几个数字的第几位数
                return int(str(firsr_num + n // digit)[n%digit])
            n -= 9*digit*firsr_num