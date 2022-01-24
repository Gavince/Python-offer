# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 下午2:27
# @Author  : gavin
# @FileName: 178.平方数之和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

示例：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

解题方法：
双指针
时间复杂度：O(sqrt(c))
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/sum-of-square-numbers/
相似题目：x的平法根、二维数据查找
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        low, high = 0, int(c**0.5)
        # 保证等号成立：c = 2
        while low <= high:
            sum_of = low*low + high * high
            if sum_of < c:
                low += 1
            elif sum_of > c:
                high -= 1
            else:
                return True
        return False