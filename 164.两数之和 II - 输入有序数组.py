# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 上午9:18
# @Author  : gavin
# @FileName: 164.两数之和II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个已按照 非递减顺序排列的整数数组numbers ，请你从数组中找出两个数满足相加
之和等于目标数target 。函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numb
ers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <=
numbers.length 。你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的
元素。

解题方法：
注意有序性，使用哈希表的时间复杂度和空间复杂度分别为O(N)
双指针
时间复杂度：O(N)
空间复杂度：O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers) - 1

        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ == target:
                return [i + 1, j + 1]
            if sum_ < target:
                i += 1
            else:
                j -= 1

        return []
