# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 上午8:27
# @Author  : gavin
# @FileName: 71..py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
剪绳子I
问题描述：
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m段（m、n都是整数，n>1并且m>1），每段绳子的
长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，
当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


剪绳子II(不同点在于大数越界问题)
问题描述：
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m段（m、n都是整数，n>1并且m>1），每段绳子的
长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，
当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

"""
import math


class Solution:

    def cuttingRope1(self, n: int) -> int:

        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)

    def cuttingRope2(self, n: int) -> int:

        if n <= 3: return n - 1
        a, b, p = n // 3, n % 3, 1000000007
        if b == 0: return 3 ** a % p
        if b == 1: return 3 ** (a - 1) * 4 % p
        return 3 ** a * 2 % p


if __name__ == "__main__":
    obj = Solution()
    print(obj.cuttingRope2(8))
    print(obj.cuttingRope2(4555))
