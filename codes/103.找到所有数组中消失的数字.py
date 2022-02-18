# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 下午6:39
# @Author  : gavin
# @FileName: 103.找到所有数组中消失的数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在
 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。进阶：你能在不使用额
 外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

解题方法：
(1)暴力法
时间复杂度：O(N)
空间复杂度：O(N)

(2)原地置换（索引与值对齐原则）
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
"""


class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        """暴力法"""
        res = []
        for val in range(1, len(nums) + 1):

            if val not in nums:
                res.append(val)

        return res

    def findDisappearedNumbers2(self, nums):
        """原地置换"""
        n = len(nums)
        for num in nums:
            # 索引对其，缺失索引值不能得到更新
            x = (num - 1) % n
            nums[x] += n
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]

        return ret


if __name__ == "__main__":
    obj = Solution()
    print(obj.findDisappearedNumbers2([1, 1, 3]))
