# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午9:32
# @Author  : gavin
# @FileName: 19.整数中1出现的次数（从1到n整数中1出现的次数）.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
求出1 ~ 13的整数中1出现的次数，并算出100 ~ 1300的整数中1出现的次数？1~13中包含1的数字
有1、10、11、12、13因此共出现6次，但是对于后面问题他就没辙了。请把问题更加普遍化，可以很
快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）
"""


class Solution:

    def countDigitOne(self, n: int) -> int:

        # 初始化
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0

        # 遍历求解
        while high != 0 or low != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            # 更新
            low += cur * digit
            cur = high % 10
            high = high // 10
            digit *= 10  # 进位

        return res
