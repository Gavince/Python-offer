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
贪心法
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/partition-labels/solution/
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # 统计每一个字符的最大右边界
        hast_table = [0] * 26
        for i, c in enumerate(s):
            hast_table[ord(c) - ord("a")] = i
        # 划分区间
        # 寻找最优边界
        res = []
        left, right = 0, 0
        for i, c in enumerate(s):
            # 扩充边界
            # 在当前区间内是否含有比当前值所在边界大的索引边界
            right = max(right, hast_table[ord(c) - ord("a")])
            if i == right:
                res.append(right - left + 1)
                left = right + 1

        return res

if __name__ == "__main__":
    obj = Solution()
    S = "ababcbacadefegdehijhklij"
    # Ｓ划分结果为 "ababcbaca", "defegde", "hijhklij"
    print(obj.partitionLabels(S))