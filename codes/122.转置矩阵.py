# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 下午3:53
# @Author  : gavin
# @FileName: 122.转置矩阵.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
	给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。矩阵的
转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

解题方法：
暴力法遍历

时间复杂度：O(m*n)
空间复杂度：O(m*n)

原题链接：
"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed