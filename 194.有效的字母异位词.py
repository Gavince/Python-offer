# -*- coding: utf-8 -*-
# @Time    : 2022/1/15 上午11:22
# @Author  : gavin
# @FileName: 194.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若s 和 t中每个字符出现的次数都相同，则称s和t互为字母异位词。

示例：
输入: s = "anagram", t = "nagaram"
输出: true

解题方法：
字符匹配
时间复杂度：O(s) s为匹配字符长度
空间复杂度：O(S) S为总26长度

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 不相等，直接为False
        if len(s) != len(t):
            return False
        record = [0]*26
        # 记录标签值
        for i in range(len(s)):
            record[ord(s[i]) - ord("a")] += 1
            record[ord(t[i]) - ord("a")] -= 1
        # 判断是否满足条件
        for i in range(26):
            if record[i] != 0:
                return False

        return True