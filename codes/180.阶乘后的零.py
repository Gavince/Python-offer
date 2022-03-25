# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 上午10:37
# @Author  : gavin
# @FileName: 180.阶乘后的零.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给定一个整数 n ，返回 n! 结果中尾随零的数量。
提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

解题方法：
归纳总结
1. 肯定不可能真去把 n! 的结果算出来，阶乘增长可是比指数增长都恐怖
2. 两个数相乘结果末尾有 0，一定是因为两个数中有因子 2 和 5，因为 10 = 2 x 5
3. 也就是说，问题转化为：n! 最多可以分解出多少个因子 2 和 5
4. 举例来说，n = 25，那么 25! 最多可以分解出几个 2 和 5 相乘？这个主要取决于能分解出几个因子 5，因为每个
偶数都能分解出因子 2，因子 2 肯定比因子 5 多得多
5. 现在，问题转化为：n! 最多可以分解出多少个因子 5
6. 假设 n = 125，来算一算 125! 的结果末尾有几个 0
7. 125 / 5 = 25，这一步就是计算有多少个像 5，15，20，25 这些 5 的倍数，它们一共可以提供一个因子 5
8. 像 25，50，75 这些 25 的倍数，可以提供两个因子 5，那么我们再计算出 125! 中有 125 / 25 = 5 个 25 的倍
数，它们每人可以额外再提供一个因子 5
9. 我们发现 125 = 5 x 5 x 5，像 125，250 这些 125 的倍数，可以提供 3 个因子 5，那么我们还得再计算出 125!
中有 125 / 125 = 1 个 125 的倍数，它还可以额外再提供一个因子 5
10.125! 最多可以分解出 25 + 5 + 1 = 31 个因子 5，也就是说阶乘结果的末尾有 31 个 0

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/
"""


class Solution:
    def trailingZeroes0(self, n: int) -> int:

        zero_cnts = 0

        for i in range(5, n + 1, 5):
            current = i
            while current % 5 == 0:
                zero_cnts += 1
                current //= 5

        return zero_cnts

    def trailingZeroes1(self, n: int) -> int:

        cnt = 0
        while n:
            cnt += n//5
            n = n // 5
        return cnt