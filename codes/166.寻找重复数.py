# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 下午6:23
# @Author  : gavin
# @FileName: 166.寻找重复数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个包含n + 1 个整数的数组nums ，其数字都在 1 到 n之间（包括 1 和 n），可知至
少存在一个重复的整数。假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。你设计的解决方
案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

解题方法：
快慢指针，环形链表
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/find-the-duplicate-number/
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if not nums: return 0
        slow, fast = 0, 0
        slow, fast = nums[slow], nums[nums[fast]]
        # 判断是否有环
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 寻找环的入口结点
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        # 返回重复数字
        return fast