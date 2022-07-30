# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 上午8:09
# @Author  : gavin
# @FileName: 210.目标和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        if abs(target) > total:
            return 0
        if (total + target) % 2 == 1:
            return 0
        # 0,1背包问题
        pos = (total + target) // 2
        neg = (total - target) // 2
        capcity = max(pos, neg)
        n = len(nums)
        # 定义dp
        # dp[i][j]表示前i个数组合为j的个数
        dp = [[0]*(capcity + 1) for _ in range(n + 1)]
        # 初始化
        for i in range(n + 1):
            dp[i][0] = 1
        # 转态转移
        for i in range(1, n + 1):
            for j in range(capcity + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                print(dp[i][j], end=" ")
            print("\n")
        # 返回值
        return dp[n][capcity]


if __name__ == "__main__":
    obj = Solution()
    obj.findTargetSumWays([1, 1, 1, 1, 1], 3)