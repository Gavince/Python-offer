# -*- coding: utf-8 -*-
# @Time    : 2021/5/3 上午8:31
# @Author  : gavin
# @FileName: 64.把數字翻譯成字符串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25
翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

实例：
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

解题方法：
动态规划
"""


class Solution:
    def translateNum(self, num: int) -> int:
        # 初始化
        strs = str(num)
        a, b = 1, 1
        for i in range(2, len(strs) + 1):
            a, b = (a + b if "10" <= strs[i - 2:i] <= "25" else a), a

        return a
