# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 上午8:26
# @Author  : gavin
# @FileName: 100.每日温度.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，
至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用0 来代替。例如，给定一个
列表temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是[1, 1,
 4, 2, 1, 1, 0, 0]。

解题方法：
（1）暴力求解
时间复杂度:O(N^2)
空间复杂度:O(N)

（2）栈(维持一个递减栈)
时间复杂度:O(N)
空间复杂度:O(N)
"""
from typing import List


class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:

        res = len(temperatures) * [0]

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break
        return res

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)
        ans = [0] * length
        # 递减栈
        stack = []
        # 遍历index进栈
        for i in range(length):
            temper = temperatures[i]
            while stack and temper > temperatures[stack[-1]]:
                pre_index = stack.pop()
                ans[pre_index] = i - pre_index
            stack.append(i)

        return ans