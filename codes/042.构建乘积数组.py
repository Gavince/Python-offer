# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 上午9:04
# @Author  : gavin
# @FileName: 42.构建乘积数组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中B[i] 的值是数组 A
中除了下标 i 以外的元素的积, 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使
用除法。

解题方法：
模拟计算方式
1.初始化：数组 B ，其中 B[0] = 1 ；辅助变量 tmp = 1 ；
2.计算 B[i] 的 下三角 各元素的乘积，直接乘入 B[i] ；
3.计算 B[i] 的 上三角 各元素的乘积，记为 tmp ，并乘入 B[i] ；
4.返回 B 。

时间复杂度：O(N)
空间复杂度：O(N)

原题链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
"""
from typing import List


class Solution:

    def constructArr(self, a: List[int]) -> List[int]:

        b, tmp = [1] * len(a), 1

        # 计算下三角(左)
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]

        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]  # 计算上三角(右)
            b[i] *= tmp  # 左右相乘(下三角乘以上三角)

        return b


if __name__ == "__main__":
    obj = Solution()
    print(obj.constructArr(a=[1, 2, 3, 4, 5]))
