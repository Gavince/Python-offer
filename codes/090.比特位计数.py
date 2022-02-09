# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 下午8:52
# @Author  : gavin
# @FileName: 90.比特位计数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。

解题方法：
时间复杂度：O(Nlog(N))
空间复杂度：O(1)
知识点：

与操作
x &=(x - 1)能够实现每一次消除最后一位1
"""


class Solution:

    def countBits(self, n: int) -> int:

        def countOnes(x):
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones

        res = [countOnes(i) for i in range( n + 1)]

        return res
