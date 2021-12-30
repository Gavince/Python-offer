# -*- coding: utf-8 -*-
# @Time    : 2021/3/4 上午9:07
# @Author  : gavin
# @FileName: 45.字符流中第一个不重复的字符.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
如：
s = "abaccdeff"
返回 "b"

s = ""
返回 " "

解题方法：
1.哈希表
字典
2.有序哈希表
"""


class Solution:

    def firstUniqueChar(self, s: str) -> bool:

        dic = {}
        for c in s:
            # 重复出现，value值为False
            dic[c] = not c in dic
        # 查询(新版本的字典是有序字典，顺序遍历)
        for k, v in dic.items():
            if v: return k

        return " "
