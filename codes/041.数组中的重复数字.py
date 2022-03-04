# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 上午9:04
# @Author  : gavin
# @FileName: 41.数组中的重复数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
    在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是
重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复
的数字。

解题方法:
方法一：
集合

方法二：
原地交换：索引与值的对应关系（一对多）

解题方法：
时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""
from typing import Tuple, Any


class Solution:

    def findRepeatNumber(self, nums: [int]) -> int:
        """"集合"""

        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)

        return -1

    def findRepeatNumber_1(self, nums: [int]) -> Tuple[Any, int]:
        """原地交换：索引与值的对应关系"""
        i = 0
        while i < len(nums):
            if nums[i] == i:  # 索引与值相对应
                i += 1
                continue

            if nums[nums[i]] == nums[i]: return nums[i], i  # 索引与值(一对多)重复
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  # 交换

        return -1


if __name__ == "__main__":
    obj = Solution()
    print(obj.findRepeatNumber_1(nums=[1, 2, 2, 4]))