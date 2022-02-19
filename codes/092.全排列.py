# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 上午8:02
# @Author  : gavin
# @FileName: 92.全排列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以
按任意顺序返回答案。

示例：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

注意:
1. 不存在有重复排列:[1, 2, 2] [1, 2, 2]， 因此不用考虑消除重复数组
2. 数组的拷贝和引用：res.append(nums[:]), res.append(nums)

原题链接：https://leetcode-cn.com/problems/permutations/
进阶题目链接:https://leetcode-cn.com/problems/permutations-ii/
"""
from typing import List


class Solution:

    def permute(self, nums):
        """不含重复数字数组的全排列"""

        res = []

        def dfs(x):
            # 回朔满足
            if x == len(nums) - 1:
                res.append(nums[:])
                return
            for i in range(x, len(nums)):
                # 交换位置
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """包含重复数字数组的全排列"""

        res = []

        def dfs(x):

            if x == len(nums) - 1:
                res.append(nums[:])
                return
            dic = set()
            for i in range(x, len(nums)):
                if nums[i] in dic: continue
                dic.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        dfs(0)
        return res

if __name__ == "__main__":
    obj = Solution()
    print(obj.permute([1, 2, 2]))
    print(obj.permuteUnique([1, 2, 2]))
