# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 下午3:19
# @Author  : gavin
# @FileName: 83.整数反转.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，
就返回 0。假设环境不允许存储 64 位整数（有符号或无符号

解题方法：
求整取余
时间复杂度:O(N)
空间复杂度:O(N)
"""


class Solution:

    def reverse(self, x: int) -> int:

        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        rev = 0
        while x != 0:
            # 边界值考虑
            if rev < INT_MIN//10 + 1 or rev > INT_MAX//10:
                return 0
            # 取余数
            # -19 % 10 = 1
            digit = x % 10
            if digit > 0 and x < 0:
                digit -= 10
            # 求整数
            # -19 // 10 = -2
            x = (x - digit) // 10

            rev = rev * 10 + digit

        return rev
