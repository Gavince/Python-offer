# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 上午8:08
# @Author  : gavin
# @FileName: 21.数组中只出现一次的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

解题方法:
1.异或
概念：参与运算的两个值，如果两个相应位相同，则结果为0，否则为1。即：0^0=0， 1^0=1，
0^1=1， 1^1=0
时间复杂度：O(N)
空间复杂度：O(1)
原题链接：https://leetcode-cn.com/problems/single-number/

2.数组在已经排好序的情况下，寻找只出现一次的数字(要求时间复杂度为Ｏ(logN))
二分查找

示例：
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

解题细节：
mid -= mid&1 (奇变偶不变)
当mid是偶数时，mid&1=0
当mid是奇数时，mid&1=1
while l <= r时，循环跳不出
时间复杂度：O(logN)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/skFtm2/
"""


class Solution:

    def singleNumber(self, nums) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a

    def singleNonDuplicate(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # 保证为偶数
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]
