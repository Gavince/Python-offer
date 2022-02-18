# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 上午8:25
# @Author  : gavin
# @FileName: 95.da.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这
个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小
偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，
今晚能够偷窃到的最高金额。

示例：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们
是相邻的。

解题方法：
	核心原则就是：第一个和最后一个不能同时抢。 所以：要么不抢第一个，要么
不抢最后一个。 注意，不抢第一个的时候，最后一个可抢可不抢；另一种情况同理
取两种情况中的最大值。因此，可以把环拆成两个队列，一个是从0到n-1，另一个
是从1到n，然后返回两个结果最大的。

注意：
此处的房屋构成一个环。
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/house-robber-ii/
"""


class Solution:

    def rob(self, nums):

        def robRange(start: int, end: int) -> int:

            first, second = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                first, second = second, max(nums[i] + first, second)

            return second

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # 头尾不能同时偷取
        # index : --> 0~n-2 1~n-1
        return max(robRange(0, len(nums) - 1), robRange(1, len(nums)))
