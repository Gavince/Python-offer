# -*- coding: utf-8 -*-
# @Time    : 2022/4/25 上午8:38
# @Author  : gavin
# @FileName: 209.最大数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

解题方法:
字符串的比较

时间复杂度：O(N^2)
空间复杂度：O(N)

原题链接:https://leetcode-cn.com/problems/largest-number/
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        res = ""
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]

        for num in nums: res += str(num)

        # 用int 消除 "00"
        return str(int(res))