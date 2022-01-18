# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 下午5:17
# @Author  : gavin
# @FileName: 174.堆排序.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    要求手写出堆排序的迭代和递归写法，并分析其时间复杂度和空间复杂度。
解题方法：
时间复杂度：O(nlog(n))
空间复杂度：O(1)
"""

class Solution:

    def heap_sort(self, nums):

        def adjust_heap(nums, start_pos, end_pos):
            new_item = nums[start_pos]
            pos = start_pos
            left_pos = pos * 2 + 1
            while left_pos < end_pos:
                right_pos = left_pos + 1
                if right_pos < end_pos and nums[right_pos] >= nums[left_pos]:
                    left_pos = right_pos
                if new_item < nums[left_pos]:
                    #　交换
                    nums[pos] = nums[left_pos]
                    pos = left_pos
                    left_pos = pos * 2 + 1
                else:
                    break
            nums[pos] = new_item

        n = len(nums)
        # 最大堆调整
        for i in reversed(range(n//2)):
            adjust_heap(nums, i, n)
        # 调整堆
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjust_heap(nums, 0, i)
        return nums


if __name__ == "__main__":
    nums = [6, 5, 3, 1, 8, 7, 2, 4]
    obj = Solution()
    print(obj.heap_sort(nums))