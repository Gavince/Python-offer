# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 下午5:27
# @Author  : gavin
# @FileName: 171.翻转字符串里的单词.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个字符串 s ，逐个翻转字符串中的所有 单词 。单词 是由非空格
字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。请你
返回一个翻转 s 中单词顺序并用单个空格相连的字符串。说明：输入字符串 s
可以在前面、后面或者单词间包含多余的空格。翻转后单词间应当仅用一个空格
分隔。翻转后的字符串中不应包含额外的空格。

示例：
输入：s = "the sky is blue"
输出："blue is sky the"

解题方法：
双指针
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:

        # 去除字符左右两边的空白
        s = s.strip()
        i, j = len(s) - 1, len(s) - 1
        res = []
        while i >= 0:
            # 有效字符
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i + 1: j + 1])
            #　消除字符间的空白
            while s[i] == " ":
                i -= 1
            j = i
        return " ".join(res)