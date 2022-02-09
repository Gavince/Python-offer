# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 下午5:27
# @Author  : gavin
# @FileName: 79.三数之和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。

解题方法:
（1）暴力求解
时间复杂度：O(N^3)
（2）二分法查找
时间复杂度：O(N^2)

注意：
返回的list中不能含有重复的列表值
如 [-1, 1, 0] [1, 0, -1]
"""
from typing import List

import numpy as np


class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])

        return np.unique(np.array(res), axis=0).tolist()

    def threeSum2(self, nums):
        """利用二分法进行数将三数之和变为两数之和"""

        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # nums已经完成排序
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            # 固定当前值
            target = -nums[i]
            # 二分算法
            left, right = i + 1, len(nums) - 1
            while left < right:
                if target == nums[left] + nums[right]:
                    res.append([nums[i], nums[left], nums[right]])
                    # 更新边界
                    left += 1
                    right -= 1
                    # 消除重复值
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif target > nums[left] + nums[right]:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.threeSum2([-1,0,1,2,-1,-4]))