# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 下午2:31
# @Author  : gavin
# @FileName: 106.回文数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给你一个整数x，如果x是一个回文整数，返回true；否则，返回false。回文
数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文
，而 123 不是。进阶：你能不将整数转为字符串来解决这个问题吗？

解题方法:
(1)字符串判断
s[::-1] == s

(2)求整得头　＝＝　求余得尾
情况１：当整数为负数时，不是回文数
eg: -121(-121和121-不相等)
情况２：当整数能够被10整除，且不为０时，不是回文数
eg: 120、112020
情况3：数字长度奇偶情况下，退出原则
while res < x:
偶数：1221
res: 1 12
x:  122 12
res == x
奇数：121
res: 1 12
x: 12 1
x = res // 10
时间复杂度：O(N)
空间复杂度:O(1)

原题链接：https://leetcode-cn.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome1(self, x: int) -> bool:

        s = str(x)
        return s == s[::-1]

    def isPalindrome2(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        res = 0
        while res < x:
            res = res * 10 + x % 10
            x = x // 10

        return x == res or x == res // 10

