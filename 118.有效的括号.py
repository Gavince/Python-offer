# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 下午9:55
# @Author  : gavin
# @FileName: 118.有效的括号.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。

解题方法：
栈
时间复杂度：O(N)
空间复杂度：O(N)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 奇数直接返回False
        if len(s) % 2: return False
        # 构建括号对
        dic = {"[": "]", "{": "}", "(": ")", "?": "?"}
        # 配对
        stack = ['?']

        for c in s:
            # 左括号进入
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False

        return len(stack) == 1