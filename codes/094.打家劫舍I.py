# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 上午10:10
# @Author  : gavin
# @FileName: 94.'.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影
响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻
的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额
的非负整数数组，计算你在不触动警报装置的情况下 ，一夜之内能够偷窃到的最
高金额。

示例：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
偷窃到的最高金额 = 1 + 3 = 4 。

解题方法：
动态规划
1. 状态定义：用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额
2. 转移方程：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
3. 初始值：dp[0], dp[1] = nums[0], max(nums[0], nums[1])
4. 返回值： dp[n] 一晚上偷窃到最高金额a
时间复杂复: O(N)
空间复杂度：O(N)

优化的动态规划：
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/house-robber/
"""


class Solution:

    def rob1(self, nums: List[int]) -> int:
        """动态规划"""

        if len(nums) == 1:
            return nums[0]

        # 定义dp
        dp = [0] * len(nums)
        # 初始化状态
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    def rob2(self, nums):
        """优化的动态规划"""

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            first, second = second, max(nums[i] + first, second)

        return second


if __name__ == "__main__":
    obj = Solution()
    print(obj.rob2([1, 2, 3, 1]))