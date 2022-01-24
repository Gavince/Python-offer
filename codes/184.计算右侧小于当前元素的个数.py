# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 上午10:18
# @Author  : gavin
# @FileName: 184.计算右侧小于当前元素的个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 nums ，按要求返回一个新数组counts 。数组 counts 有该性质：
counts[i] 的值是nums[i] 右侧小于nums[i] 的元素的数量。

示例：
输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

解题方法：
二分法构造有序序列
5 4 1
插入数字 4 --> 6 5 4 1  len(arr) -idx = 3
时间复杂度：O(Nlog(N))
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/
"""


class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n
        sort_stack = []

        def binary_search(arr, target):
            # 从大到小进行插入

            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        for i in range(n - 1, -1, -1):
            x = nums[i]
            idx = binary_search(sort_stack, x)
            counts[i] = len(sort_stack) - idx
            sort_stack.insert(idx, x)
        return counts


if __name__ == "__main__":
    obj = Solution()
    print(obj.countSmaller([2, 5, 1, 4, 6]))
