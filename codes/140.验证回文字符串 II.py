# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 上午8:16
# @Author  : gavin
# @FileName: 140.验证回文字符串 II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例:
输入: s = "aba"
输出: true

解题方法：
时间复杂度：O(|s|)
空间复杂度：O(|1|)

原题链接：https://leetcode-cn.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkpalindrome(low, high):

            while low < high:
                if s[low] == s[high]:
                    low += 1
                    high -= 1
                else:
                    return False
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 删除一个字符，判断剩余字符串是否为回文字符串
                return checkpalindrome(left + 1, right) or checkpalindrome(left, right - 1)

        return True
