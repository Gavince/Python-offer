# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 上午8:27
# @Author  : gavin
# @FileName: 51.第一个只出现一次的字符.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
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
