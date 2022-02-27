# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 上午8:39
# @Author  : gavin
# @FileName: 54.左旋转字符串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字
符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结
果"cdefgab"

示例：
输入: s = "abcdefg", k = 2
输出: "cdefgab"

解题方法：
求余数，取整数
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""


class Solution:

    def reverseSelectWords_fun1(self, s: str, n: int) -> str:
        """切片方法"""

        return s[n:] + s[:n]

    def reverseSelectWords_fun2(self, s: str, n: int) -> str:
        """遍历算法"""

        res = []
        for i in range(n, len(str) + n):
            res.append(s[i % len(s)])

        return "".join(res)

    def recverseSelectWords_fun3(self, s: str, n: int) -> str:
        """先尾后头法"""

        res = []
        # 尾部
        for i  in range(n, len(str)):
            res.append(str[i])
        # 头部
        for i in range(n):
            res.append(str[i])

        return "".join(res)
