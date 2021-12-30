# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 上午9:16
# @Author  : gavin
# @FileName: 53.和为S的连续正数序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两
个数）。序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

实例：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

解题方法：
1. 初始化： 左边界 i = 1 ，右边界 j = 2 ，元素和 s = 3 ，结果列表 res；
2. 循环： 当 i ≥ j 时跳出；
    当 s > targets 时： 向右移动左边界 i = i + 1 ，并更新元素和 s；
    当 s < targets 时： 向右移动右边界 j = j + 1，并更新元素和 s；
    当 s = targets 时： 记录连续整数序列，并向右移动左边界 i = i + 1，并更新元素和 s；
3. 返回值： 返回结果列表 res ；
"""


class Solution:

    def findContinuousSequence(self, target):

        # 初始化连续区间
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j+1)))
            if s >= target:
                s -= i  # 先减后加
                i += 1
            else:
                j += 1  # 先加后减
                s += j

        return res