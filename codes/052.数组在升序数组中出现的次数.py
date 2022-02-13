# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 上午9:35
# @Author  : gavin
# @FileName: 52.在排序数组中查找数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
统计一个数字在排序数组中出现的次数

实例：
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

解题方法：
二分法排序

时间复杂度：O(log(N))
空间复杂度：O(1)

原题链接：
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
"""


class Solution:

    def BinarySearch(self, array, t):
        # 二分查找算法必须有序

        low = 0
        height = len(array) - 1

        while low <= height:
            mid = (low + height) // 2
            if array[mid] > t:
                height = mid - 1
            elif array[mid] < t:
                low = mid + 1
            else:
                return array[mid]
        return -1

    def serach(self, nums: [int], target: int) -> int:
        """搜索指定的重复数字"""

        def helper(tar):
            """查找指定值的右边界"""
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2

                if nums[mid] <= tar:
                    i = mid + 1
                else:
                    j = mid - 1

            return i  # 返回右边界索引

        return helper(target) - helper(target - 1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.BinarySearch([1, 2, 5, 7, 20], 20))
