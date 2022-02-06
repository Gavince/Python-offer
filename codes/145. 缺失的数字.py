# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 下午4:41
# @Author  : gavin
# @FileName: 145. 缺失的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个包含 [0, n]中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在
数组中的那个数。
进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
解题方法：
(1)位运算
异或操作
时间复杂度：O(N)
空间复杂度：O(1)

(2)求和公式
Sn = (n*(a1 + an))/2
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/missing-number-lcci/
"""


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:

        if not nums:
            return 0

        missing_num = len(nums)
        # 异或操作，保留最后的值
        for i, num in enumerate(nums):
            missing_num ^= (num ^ i)

        return missing_num

    def missingNumber2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        exp_num = (len(nums) * (len(nums) + 1)) // 2
        act_num = sum(nums)

        return exp_num - act_num
