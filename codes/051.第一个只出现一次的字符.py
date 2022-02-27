# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 上午8:27
# @Author  : gavin
# @FileName: 51.第一个只出现一次的字符.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含
小写字母。
解题方法:
字典遍历
示例：
输入：s = "abaccdeff"
输出：'b'

时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""


import collections


class Solution:

    def firstUniqueChar(self, s):
        dic = collections.OrderedDict()

        for c in s:
            # 重复出现为False
            dic[c] = not c in dic
        for k, v in dic:
            if v: return k
        return " "
