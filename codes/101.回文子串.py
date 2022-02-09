# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 上午9:23
# @Author  : gavin
# @FileName: 101.回文子串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被
视作不同的子串。

解题方法：
（1）中心扩散法（注意偶数扩散和奇数扩散）
方法在奇数下不能使用单个中心点得到偶数下的回文子串，因此，需要将
偶数和奇数进行分别处理，高阶奇偶变化可以由低阶奇偶有限次扩展得到。
时间复杂度:O(N^2)
空间复杂度：O(1)

（2）中心扩散法（消除奇偶，单层循环处理）
枚举所有可能的中心点，有2*n - 1个中心点（共有n 个奇数中心点和n - 1个偶数中心点）
时间复杂度:O(N^2)
空间复杂度：O(1)

原题链接:https://leetcode-cn.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings1(self, s: str) -> int:

        def speard(l, r):
            """中心扩散"""
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        res = 0
        # 奇数中心扩散
        for i in range(len(s)):
            res += speard(i, i)
        # 偶数中心扩散
        for i in range(len(s) - 1):
            res += speard(i, i + 1)

        return res

    def countSubstrings2(self, s: str) -> int:

        n = len(s)
        ans = 0

        for i in range(2*n - 1):
            l, r = i//2, i//2 + i%2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                ans += 1
        return ans