# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 上午8:39
# @Author  : gavin
# @FileName: 141.最长回文串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造
成的最长的回文串。在构造过程中，请注意区分大小写。比如"Aa"不能当
做一个回文字符串。注意:假设字符串的长度不会超过 1010。

示例：
输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

解题方法：
哈希表

原题链接：https://leetcode-cn.com/problems/longest-palindrome/
"""


class Solution:
    """不变动"""
    def longestPalindrome(self, s: str) -> int:
        # 中心扩展法
        def spread(l, r):

            count = 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 2

            return count

        res = 0
        strs = list(s)
        # 奇数中心
        for i in range(len(strs)):
            res = max(res, spread(i, i))
        # 偶数中心
        for i in range(len(strs) - 1):
            res = max(res, spread(i, i + 1))

        return res


import collections


class Solution1:
    """重新构建"""
    def longestPalindrome(self, s: str) -> int:

        count = collections.Counter(s)
        ans = 0

        for v in count.values():
            # 偶数个数全添加
            ans += v // 2 * 2
            # 偶数中间添加奇数
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1

        return ans