# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 下午8:56
# @Author  : gavin
# @FileName: 80.无重复字符的最长子串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

解题方法：
滑动窗口
两种情况下滑动窗口的移动：
（1）[abcdef]a  ----> [bcdefa]
（2）[bdefa]a  ----> [a]

时间复杂度：O(N)
空间复杂度：O(N) 使用集合临时存储了最长字符串，极端情况下需要存储N

原题链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s: return 0
        # left 记录窗口左边界索引值
        left, max_len, cur_len = 0, 0, 0
        look_up = set()

        for i in range(len(s)):
            cur_len += 1
            # 循环判断，直到左边界唯一
            while s[i] in look_up:
                look_up.remove(s[left])
                left += 1
                cur_len -= 1
            # 记录字符串最长长度
            if cur_len > max_len: max_len = cur_len
            look_up.add(s[i])

        return max_len
