# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 上午9:06
# @Author  : gavin
# @FileName: 44.表示数值的字符串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

解题方法：

"""


class Solution:

    def isNumber(self, s: str) -> bool:
        # 总共八种状态
        # 构建状态转移表
        states = [
            {" ": 0, "s": 1, "d": 2, ".": 4},
            {"d": 2, ".": 4},
            {"d": 2, "e": 5, ".": 3, " ": 8},
            {"d": 3, "e": 5, " ": 8},
            {"d": 3},
            {"s": 6, "d": 7},
            {"d": 7},
            {"d": 7, " ": 8},
            {" ": 8}
        ]

        p = 0
        for c in s:
            if "0" <= c <= "9": t = "d"
            elif c in "+-": t = "s"
            elif c in "eE": t = "e"
            elif c in ". ": t = c
            else: t = "?"  # 非数值

            if t not in states[p]: return False
            p = states[p][t]
        return  p in (2, 3, 7, 8)  # 正常退出状态
