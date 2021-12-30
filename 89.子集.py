# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 上午8:29
# @Author  : gavin
# @FileName: 83.子集.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有
可能的子集（幂集）。解集不能包含重复的子集。你可以按 任意顺序 返回解集。

实例：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

解题方法：
时间复杂度：

空间复杂度：

注意：
空集是任何形式的子集。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """迭代法"""

        res = [[]]
        for i in range(len(nums) - 1, -1, -1):
            # 在原有子集的基础上，增加新的元素构成新的子集
            for subres in res[:]: res.append(subres + [nums[i]])

        return res

    def subsets(self, nums):
        """回朔法"""
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            # 横向遍历
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res
