# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 上午10:36
# @Author  : gavin
# @FileName: 179.轮转数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
（注意：使用O(1)的空间复杂度）
示例：
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

解题方法：
局部翻转排序算法
一次整体翻转 + 两次局部翻转
时间复杂度：O(n)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/rotate-array/
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        k %= n
        # 整体翻转
        reverse(0, n - 1)
        # 左半部分
        reverse(0, k - 1)
        # 有半部分
        reverse(k, n - 1)