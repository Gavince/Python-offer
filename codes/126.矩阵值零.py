# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 下午9:21
# @Author  : gavin
# @FileName: 126..py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：

    给定一个m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为0。
请使用原地算法。
进阶：
    一个直观的解决方案是使用 O(mn)的额外空间，但这并不是一个好的解决方案。一个简
单的改进方案是使用 O(m+n) 的额外空间，但这仍然不是最好的解决方案。你能想出一个仅
使用常量空间的解决方案吗？

解题方法：
方法一：
设置行列标记，行标记或者列标记为零时，元素置为零。
时间复杂度：O(MN)
空间复杂度：O(M + N)

方法二：
只存储有效的行列标记
时间复杂度：O(MN)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/set-matrix-zeroes/
"""


class Solution:

    def setZeroesfor1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 初始化
        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n

        # 设置标记
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = cols[j] = True

        # 置零
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

    def setZeroesfor2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        row_zeros, col_zeros = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)

        for i in range(m):
            for j in range(n):
                if i in row_zeros or j in col_zeros:
                    matrix[i][j] = 0
