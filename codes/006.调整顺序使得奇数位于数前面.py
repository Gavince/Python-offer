# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 下午7:39
# @Author  : gavin
# @FileName: 6.调整顺序使得奇数位于数前面.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇
数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶
数和偶数之间的相对位置不变。

解决方案：
快慢指针
fast：快指针实现遍历，标志奇数位置
slow：慢指针实现对偶数位置进行表示
时间复杂度：O(N)
空间复杂度：O(1)
"""


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:

        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # 标志偶数位值
                slow += 1
            # 标志奇数位置，并实现遍历
            fast += 1

        return nums