# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 下午8:03
# @Author  : gavin
# @FileName: 162.字符串相加.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符
串转换为整数形式。

解题方法：
双指针
时间复杂度：O(max(m, n))
空间复杂度：O(1)
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            # 求解进位
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1

        return "1" + res if carry else res
