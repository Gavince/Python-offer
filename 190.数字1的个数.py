# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 上午10:48
# @Author  : gavin
# @FileName: 190.数字1的个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

解题方法：
数学推导
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/number-of-digit-one/
"""


class Solution:
    def countDigitOne(self, n: int) -> int:

        dight, res = 1, 0
        cur, low, high = n % 10, 0, n // 10
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * dight
            elif cur == 1:
                res += high * dight + 1 + low
            else:
                res += high * dight + dight
            # 更新位置
            low += cur * dight
            cur = high % 10
            high = high // 10
            dight = dight * 10

        return res