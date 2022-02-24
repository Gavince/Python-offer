# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 上午10:10
# @Author  : gavin
# @FileName: 66.最长不含重复字符的子字符串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

实例：
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

注意：
最长不含重复子串的长度

原题链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:

    def lengthOfLongsetSubstring(self, s: str) -> int:

        # 字典存储索引值
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            # 获取i索引，默认值为-1
            i = dic.get(s[j], -1)
            # update
            dic[s[j]] = j
            # 状态转移
            tmp = tmp + 1 if j - i > tmp else j - i
            res = max(tmp, res)

        return res