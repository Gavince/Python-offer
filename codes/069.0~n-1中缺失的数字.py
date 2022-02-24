# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 上午8:45
# @Author  : gavin
# @FileName: 69.0~n-1中缺失的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范
围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找
出这个数字。

解题方法：
递增排序数组－＞二分法

注意：
有且只有一个数字不在数组中

时间复杂度：O(logN)
空间复杂度：O(1)
0 1 2  4 5
m = 2
num[2] = 2
i = 3
j = 4
m = 3
num[3] != 3
i = 3
j = 3
m = 3
num[3] != 3
i = 3
j = 2
return 3
原题链接：

"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """二分法"""

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1

        return i