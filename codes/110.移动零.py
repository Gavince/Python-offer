# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 下午9:32
# @Author  : gavin
# @FileName: 110.移动零.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持
非零元素的相对顺序。

要求：
(1) 必须在原数组上操作，不能拷贝额外的数组。
(2) 尽量减少操作次数。

示例：
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

解题方法：
１．暴力法：
时间复杂度：O(N)
空间复杂度：O(N)

２．双指针
首次快慢指针分离之后：
slow 始终指向第一个为零的数组的位置
fast 始终指向不为零的数组位置
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：
"""


class Solution:

    def moveZeros1(self, nums):
        """暴力法"""

        j = 0
        tmp_array = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp_array[j] = nums[i]
                j += 1

        nums = tmp_array[:]

    def moveZeros2(self, nums):
        """双指针"""

        fast = slow = 0
        while fast < len(nums):
            # slow 指向第一个不为零的位置
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
