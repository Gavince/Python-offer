# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 上午9:00
# @Author  : gavin
# @FileName: 102.根据身高重建队列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不
一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面正好
 有 ki 个身高大于或等于 hi 的人。请你重新构造并返回输入数组people 所表示的队列
 。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j
 个人的属性（queue[0] 是排在队列前面的人）。
"""


class Solution:

    def reconstructQueue1(self, people):

        res = []
        # h_i: decrease
        # k_i: increase
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in people:
            if p[1] >= len(res):
                res.append(p)
            elif p[1] < len(res):
                res.insert(p[1], p)

        return res

    def reconstructQueue2(self, people):

        people = sorted(people, key=lambda x: (x[0], x[1]))
        i = 0
        while i < len(people):
            if i > people[i][1]:
                # insert->delete
                people.insert(people[i][1], people[i])
                people.pop(i + 1)
            i += 1
        return people
