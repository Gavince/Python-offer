# -*- coding: utf-8 -*-
# @Time    : 2022/3/12 上午11:04
# @Author  : gavin
# @FileName: 205.搜索排序数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多
次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。
注意: 若有多个相同元素，返回索引值最小的一个。


示例：
输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],
target = 5
输出: 8（元素5在该数组中的索引）

解题方法：
二分法
时间复杂度：O(logN)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/search-rotate-array-lcci/
"""


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # 二分法算法下进行部分有序查找
        if not arr: return -1
        left, right = 0, len(arr) - 1
        while left <= right:
            # 1 1 1 2 1 target:1
            if arr[left] == target:
                return left
            mid = (left + right) // 2
            # 1 2 2 1 1 target:2
            if arr[mid] == target:
                right = mid
            # 1 2 3 4 5 target:2
            elif arr[0] < arr[mid]:
                if arr[0] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 4 5 1 2 3 target:2
            elif arr[0] > arr[mid]:
                if arr[mid] < target <= arr[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 1 1 1 1 2 1 target:2
            else:
                left += 1
        return -1
