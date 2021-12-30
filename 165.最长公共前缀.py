# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 上午8:36
# @Author  : gavin
# @FileName: 165.最长公共前缀.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共
前缀，返回空字符串 ""。
实例1:
输入：strs = ["flower","flow","flight"]
输出："fl"
实例2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
解题方法：
纵向比较
时间复杂度：O(MN)
空间复杂度：O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            # 比较剩余部分
            if any(i == len(strs[j]) or c != strs[j][i] for j in range(1, count)):
                return strs[0][:i]

        # 只有一个字符时
        return strs[0]