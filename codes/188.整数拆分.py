# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午10:18
# @Author  : gavin
# @FileName: 188.整数拆分.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的
乘积最大化。 返回你可以获得的最大乘积。


解题方法：
数学推导, 几何平均值
时间复杂度：O(1)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/integer-break/
"""


class Solution:
    def integerBreak(self, n: int) -> int:

        if n <= 3: return n - 1
        # 求解整数和余数
        a, b = n//3, n%3
        if b == 0: return 3**(a)
        if b == 1: return 3**(a - 1)*4
        return 3**(a)*2