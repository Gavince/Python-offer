# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 上午8:39
# @Author  : gavin
# @FileName: 55.翻转单词顺序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。

解题方法：
1. 倒置排序

注意：
while 表示：
i = 0 时，字符为“I”还需要进行遍历
下一步：i = -1，退出while循环，返回倒转结果
"""


class Solution:

    def reverseWords(self, s:str) -> str:
        """双指针法"""

        # 消除首尾空格
        s = s.strip()
        i = j = len(str) - 1
        res = []
        while i >= 0:
            # 搜索单词首字符
            while i >= 0 and s[i] != " ": i -= 1
            res.append(s[i+1: j+1])
            while s[i] == " ": i -= 1
            j = i
        return " ".join(res)

    def reverseWords(self, s:str) -> str:

        return " ".join(s.strip().split()[::-1])  # 分割倒置