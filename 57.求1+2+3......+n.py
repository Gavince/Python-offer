# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 上午8:13
# @Author  : gavin
# @FileName: 57.求1+2+3......+n.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

解题方法：
递归，并使用逻辑运算
"""


class Solution:

    def __init__(self):
        self.res = 0

    def sunNums(self, n: int) -> int:
        """递归求和"""

        n > 1 and self.sunNums(n - 1)
        self.res += n
        return  self.res