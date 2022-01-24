# -*- coding: utf-8 -*-
# @Time    : 2022/1/15 上午9:42
# @Author  : gavin
# @FileName: 193.字符串解码.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，
表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数，你可以认为
输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。此外，
你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的
输入。

示例：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

解题方法：
栈
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/decode-string/
"""

class Solution:
    def decodeString(self, s: str) -> str:

        stack, res, multi = [], "", 0
        for c in s:
            if c == "[":
                stack.append([res, multi])
                # 重置
                res, multi = "", 0
            elif c == "]":
                # 3[a4[bcd]]
                last_res, cur_multi = stack.pop()
                res = last_res + cur_multi*res
            elif "0" <= c <= "9":
                # 进位运算， eg:121
                multi = multi*10 + int(c)
            else:
                res += c
        return res