# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 上午10:10
# @Author  : gavin
# @FileName: 186.划分字母区间.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    字符串 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母
最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

解题方法：
贪心法（保证各个切分的子段不存在字符交集）
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/partition-labels/solution/
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # 存放每一个字符的最右边界
        hash_tabel = [0] * 26
        for i, c in enumerate(s):
            hash_tabel[ord(c) - ord("a")] = i
        # 　遍历寻找切分数组
        res = []
        left, right = 0, 0
        for idx, c in enumerate(s):
            # 当前子段的最右边界被替换
            right = max(right, hash_tabel[ord(c) - ord("a")])
            if idx == right:
                res.append(right - left + 1)
                left = right + 1
        return res


if __name__ == "__main__":
    obj = Solution()
    S = "ababcbacadefegdehijhklij"
    # Ｓ划分结果为 "ababcbaca", "defegde", "hijhklij"
    print(obj.partitionLabels(S))
