# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 上午8:26
# @Author  : gavin
# @FileName: 50.把数组排成最小的数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

实例：
输入: [3,30,34,5,9]
输出: "3033459

说明：
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导0

解题方法：
快速排序法
"""


class Solution:

    def quick_sort(self, nums, start, end):
        """实现快速排序法"""

        if start >= end:
            return

        # 基准数据
        mid = nums[start]
        low = start
        high = end

        while low < high:
            # 右半部分大(注意边界条件，右半部分个大于等于)
            while low < high and nums[high] >= mid:
                high -= 1
            nums[low] = nums[high]

            while low < high and nums[low] < mid:
                low += 1
            nums[high] = nums[low]

        # 交换分界线
        nums[low] = mid
        # 左半部分(递归调用)
        self.quick_sort(nums, start, low - 1)
        self.quick_sort(nums, low + 1, end)

    def minNumber(self, nums):

        def quick_sort(l, r):

            if l >= r: return
            low, hight = l, r

            while low < hight:
                while strs[hight] + strs[l] >= strs[l] + strs[hight] and low < hight: hight -= 1
                while strs[low] + strs[l] <= strs[l] + strs[low] and low < hight: low += 1
                strs[low], strs[hight] = strs[hight], strs[low]

            strs[low], strs[l] = strs[l], strs[low]
            quick_sort(l, low - 1)
            quick_sort(low + 1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)

        return "".join(strs)


if __name__ == '__main__':
    obj = Solution()
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    obj.quick_sort(alist, 0, len(alist) - 1)
    # obj.minNumber(alist)
    print(alist)
