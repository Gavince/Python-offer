# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 上午9:20
# @Author  : gavin
# @FileName: 199.螺旋矩阵II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序
螺旋排列的 n x n 正方形矩阵 matrix 。

解题方法：
模拟螺旋矩阵的运行方式

时间复杂度：O(MN)
空间复杂度：O(MN)

原题链接：https://leetcode-cn.com/problems/spiral-matrix-ii/
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        tar = n*n
        num = 1
        # 申请矩阵进行存储
        mat = [[0]*n for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        while tar >= num:
            # 从左向右进行遍历
            for i in range(l, r + 1):
                mat[t][i] = num
                num += 1
            t += 1
            # 从上向下进行遍历
            for i in range(t, b + 1):
                mat[i][r] = num
                num += 1
            r -= 1
            # 从右向左进行遍历
            for i in range(r, l, -1):
                mat[b][i] = num
                num += 1
            b -= 1
            # 从下向上进行遍历
            for i in range(b, t, -1):
                mat[i][l] = num
                num += 1
            l += 1

        return mat
