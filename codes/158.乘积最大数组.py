# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 上午8:34
# @Author  : gavin
# @FileName: 158.乘积最大数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）
，并返回该子数组所对应的乘积。

实例：
输入: [2,3,-2,4]
输出: 6

解题方法：
    需要注意正负号的变化，特别是最小负数值的保存，在遇见下一个负数值时，会变成当前足最大的
数值（负负得正）。
pre_max: 2 pre_min: 2
cur_max: 6 cur_min: 3
cur_max:-2 cur_min: -12
cur_max: 4 cur_min: -48

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/maximum-product-subarray/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        pre_min, pre_max = nums[0], nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(pre_min * nums[i], pre_max * nums[i], nums[i])
            cur_min = min(pre_min * nums[i], pre_max * nums[i], nums[i])
            ans = max(cur_max, ans)
            print("cur_max:", cur_max, "cur_min:", cur_min)
            pre_max = cur_max
            pre_min = cur_min

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProduct(nums=[2, 3, -2, 4]))
