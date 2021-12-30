# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 下午3:52
# @Author  : gavin
# @FileName: 2.二维数据查找.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增
的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样
的一个二维数组和一个整数，判断数组中是否含有该整数,形式如下:
1  2  3  4
2  3  4  5
6  7  8  9
10 11 12 13

解决方案：
时间复杂度：O(M + N), M和N为行数和列数
空间复杂度：O(1)，没有使用额外的空间存储
"""


class Solution:

    def findNumberIn2DArray(self, matrix, target):
        """在二维数组中找到指定数字"""

        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True

        return False
