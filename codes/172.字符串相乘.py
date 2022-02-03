# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 下午5:14
# @Author  : gavin
# @FileName: 172.字符串相乘.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，
它们的乘积也表示为字符串形式。

解题方法：
时间复杂度：O(mn)
空间复杂度：O(m + n)
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """模拟乘法运算"""

        # 申请额外空间进行运算
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        ansArr = [0]*(m + n)
        # 模拟运算 高位在前，低位在后
        for i in range(m  - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x*int(num2[j])

        for i in range(m + n - 1, 0, -1):
                ansArr[i - 1] += ansArr[i] // 10
                ansArr[i] %= 10
        index  = 1 if ansArr[0] == 0 else 0

        return "".join( str(i) for i in ansArr[index:])