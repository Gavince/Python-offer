# -*- coding: utf-8 -*-
# @Time    : 2021/3/3 上午10:17
# @Author  : gavin
# @FileName: 43.正则表达式匹配.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
"""


class Solution:

    def isMathch(self, s: str, p: str) -> bool:

        if not p: return not s
        # 首字符匹配
        first_match = bool(s and p[0] in {s[0], "."})

        # 如果第二个字符为"*"，则分为“*”字符前字符出现零次或一次以上两种情况
        if len(p) >= 2 and p[1] == "*":
            return self.isMathch(s, p[2:]) \
                   or first_match and self.isMathch(s[1:], p)
        else:
            return first_match and self.isMathch(s[1:], p[1:])
