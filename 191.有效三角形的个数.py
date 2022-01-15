# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 上午10:50
# @Author  : gavin
# @FileName: 191.有效三角形的个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形
三条边的三元组个数。

解题方法：
原则：两边之和大于第三边

方法一：二分法
数组排序后满足：a <= b <= c
一定存在：a + c > b，b + c > a
需要证明：c < a + b
二分法寻找可能的c值
时间复杂度：O(n^2logn)
空间复杂度：O(logn)

方法二：双指针
时间复杂度：O(n^2)
空间复杂度：O(logn)
"""
from typing import List


class Solution:
    def triangleNumberofBinarySort(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                # 使用二分法查找第三个数字
                left, right, k = j + 1, n - 1, j
                # 在有序数组中寻找目标值
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j

        return ans

    def triangleNumberofDoublePoint(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                # 遍历第三个结点c
                # a, b, k + 1
                # 1, 2, 3, 5, 7, 9
                while k + 1 < n and nums[k + 1] < nums[j] + nums[i]:
                    k += 1
                ans += max(k - j, 0)

        return ans


