# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 上午9:50
# @Author  : gavin
# @FileName: 47.数值的整数次方.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

解题方法：
快速幂解析
2^5 = (2^2)^2*2

注意：
奇数&1＝１
偶数＆1=0
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:

        if x == 0: return 0
        res = 1  # 存储计算数

        # 负数变为正数计算
        if n < 0: x,  n = 1/x,  -n
        while n:
            if n&1: res *= x  # 等价n%2
            x *= x
            n >>= 1  # 等价ｎ//2

        return res
