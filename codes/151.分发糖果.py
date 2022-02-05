# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 上午10:43
# @Author  : gavin
# @FileName: 151.分发糖果.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    老师想给孩子们分发糖果，有 N个孩子站成了一条直线，老师会根据每个孩
子的表现，预先给他们评分。你需要按照以下要求，帮助老师给这些孩子分发糖果
：每个孩子至少分配到 1 个糖果。评分更高的孩子必须比他两侧的邻位孩子获得
更多的糖果。那么这样下来，老师至少需要准备多少颗糖果呢？

解题方法：
双指针
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/candy/
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:

        left = [1 for _ in range(len(ratings))]
        right = left[:]
        # 左遍历
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        cnt = left[-1]

        # 右遍历
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

            cnt += max(left[i], right[i])

        return cnt
