# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 上午8:06
# @Author  : gavin
# @FileName: 73.不用加减乘除做加法.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/”
四则运算符号。


解题方法：
位运算
n = a^b  # 异或
c = (a & b) << 1  #　与并左移进位
s = n + c

注意：
负数的处理


"""


class Solution:

    def  aad(self, a: int, b: int) -> int:

        x = 0xffffffff
        a, b = a & x, b & x  # 截断高位

        while b:
            a, b = (a^b), (a & b) << 1 & x

        return a if a <= 0x7fffffff else ~(a^x)  # 负数高位(32)取反,低位保持不变