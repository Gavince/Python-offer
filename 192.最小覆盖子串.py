# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 上午9:52
# @Author  : gavin
# @FileName: 192.最小覆盖子串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果
s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
- 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
- 如果 s 中存在这样的子串，我们保证它是唯一的答案。

解题方法：
滑动窗口

原题链接：https://leetcode-cn.com/problems/minimum-window-substring/
"""
import collections


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        # 初始化need字典
        for c in t:
            need[c] += 1
        # 统计还需要的数目
        needCnt = len(t)
        left = 0
        res = (0, float("inf"))

        # 滑动窗口
        for right, c in enumerate(s):
            # right
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1

            # 滑动左窗口，并消除多余数目
            if needCnt == 0:
                while True:
                    c = s[left]
                    # a, a
                    if need[c] == 0:
                        break
                    need[c] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                # 寻找下一个位置
                need[s[left]] += 1
                needCnt += 1
                left += 1

        return "" if res[1] > len(s) else s[res[0]: res[1] + 1]