# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 上午9:14
# @Author  : gavin
# @FileName: 138.数组中的逆序对.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例：
输入: [7,5,6,4]
输出: 5

解题方法：
归并排序
时间复杂度：O(NlogN)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
"""


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.merge_sort(nums)
        return self.cnt

    def merge_sort(self, nums):

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):

        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            # 严格大于
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                self.cnt += (len(left) - i)
        res += left[i:]
        res += right[j:]

        return res
