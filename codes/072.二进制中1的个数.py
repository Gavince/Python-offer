# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 下午8:23
# @Author  : gavin
# @FileName: 72.二进制中1的个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9
表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

"""

class Solution:

    def hammingweight1(self, n: int) -> int:
        """逐位相与"""

        res = 0
        while n:
            res += n&1
            n >>= 1

        return res
    def hammingweight2(self, n: int) -> int:

        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res