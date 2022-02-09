# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 下午10:16
# @Author  : gavin
# @FileName: 87.翻转二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个 n×n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转90度。
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一
个矩阵来旋转图像。

解题方法：
(1) 暴力解法
时间复杂度：O(N^2)
空间复杂度：O(N^2)
(2)旋转法
时间复杂度：O(N^2)
空间复杂度：O(1)

注意：
题目要求必须在原地旋转图像
"""


class Solution:

    def rotate1(self, matrix):
        """暴力求解"""

        n = len(matrix)
        # 构建临时旋转矩阵
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]

        matrix[:] = matrix_new

    def rotate2(self, matrix):
        """旋转变换"""

        T, L, B, R = 0, 0, len(matrix) - 1, len(matrix) - 1
        # k为旋转次数
        move = len(matrix)
        for k in range(len(matrix) // 2):
            for i in range(move - 1):
                matrix[T][L + i], matrix[T + i][R] = matrix[T + i][R], matrix[T][L + i]
                matrix[T][L + i], matrix[B][R - i] = matrix[B][R - i], matrix[T][L + i]
                matrix[T][L + i], matrix[B - i][L] = matrix[B - i][L], matrix[T][L + i]

            T += 1
            L += 1
            B -= 1
            R -= 1
            move -= 2


if __name__ == "__main__":
    obj = Solution()
    m = [[1,2,3],[4,5,6],[7,8,9]]
    obj.rotate2(m)
    print(m)