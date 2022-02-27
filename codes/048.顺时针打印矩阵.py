# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 上午9:50
# @Author  : gavin
# @FileName: 48.顺时针打印矩阵.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


解题方法：
方法1:
zip使用旋转矩阵
 ma
[[4, 5, 6], [7, 8, 9]]
list(zip(*ma))
[(4, 7), (5, 8), (6, 9)]
list(zip(*ma))[::-1]
[(6, 9), (5, 8), (4, 7)]

方法2:
边界条件

原题链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
"""
from typing import List


class Solution:

    def spiralOrder(self, matirx: List[List[int]]) -> List[int]:

        res = []
        while matirx:
            res += matirx.pop(0)
            # 旋转数组
            matirx = list(zip(*matirx))[::-1]

        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix: return []
        res = []
        #  输入边界条件
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while True:
            # 从左向右
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1
            if t > b: break
            # 从上之下
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if r < l: break
            # 从右向左
            for i in range(r, l - 1, -1): res.append(matrix[b][i])
            b -= 1
            if b < t: break
            # 从下之上
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break

        return res


if __name__ == "__main__":
    obj = Solution()
    ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(obj.spiralOrder(ma))
