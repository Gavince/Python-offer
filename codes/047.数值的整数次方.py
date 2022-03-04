# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 上午9:50
# @Author  : gavin
# @FileName: 47.数值的整数次方.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。

解题方法：
快速幂解析
注意：需要将负数转换为正数进行处理
2^5 = (2^2)^2*2
step1:
n == 5
res = 2 * 1
x = 2 * 2
step2:
n == 2
res = 2 * 2
x = (2 * 2)**2
step3:
n == 1
res = 2 ** 5
step:4
n == 0
退出
原题链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:

        if x == 0: return 0
        res = 1  # 存储计算数

        # 负数变为正数计算
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x  # 等价n%2
            x *= x
            n >>= 1  # 等价ｎ//2

        return res
