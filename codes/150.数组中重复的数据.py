# -*- coding: utf-8 -*-
# @Time    : 2021/9/19 下午9:49
# @Author  : gavin
# @FileName: 150.数组中重复的数据.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素
出现两次而其他元素出现一次。找到所有出现两次的元素。你可以不用到任何额外空
间并在O(n)时间复杂度内解决这个问题吗？

解题方法：
使用符号进行标记，下次出现可用符号变化进行判断
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        if not nums: return []

        res = []
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res