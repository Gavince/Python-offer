# -*- coding: utf-8 -*-
# @Time    : 2021/12/7 下午6:14
# @Author  : gavin
# @FileName: 168.下一个排列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下
一个更大的排列（即，组合出下一个更大的整数）。如果不存在下一个更大的排列，则
将数字重新排列成最小的排列（即升序排列）。必须原地修改，只允许使用额外常数空间。

解题方法：
１．先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
２．再找出另一个最大索引 l 满足 nums[l] > nums[k]；
３．交换 nums[l] 和 nums[k]；
４．最后翻转 nums[k+1:]。

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-powcai/
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        first_index = -1
        n = len(nums)

        def reverse(nums, i, j):
            """翻转列表（双指针）"""

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # 条件1
        # 选择以第一个最大的index(倒排查找)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break

        # 已经是最大值[3, 2, 1]
        if first_index == -1:
            reverse(nums, 0, n - 1)
            return
        # 条件2
        second_index = -1
        for i in range(n - 1, first_index, -1):
            if nums[i] > nums[first_index]:
                second_index = i
                break
        # 交换
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        reverse(nums, first_index + 1, n - 1)
