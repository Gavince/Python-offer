# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 下午3:55
# @Author  : gavin
# @FileName: 125.对角线遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
	给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回
这个矩阵中的所有元素，对角线遍历如下图所示。

解题方法:
遍历

时间复杂度：O()
空间复杂度：O()

原题链接：https://leetcode-cn.com/problems/diagonal-traverse/
"""
import collections


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        dic = collections.defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i + j].append(mat[i][j])

        # 蛇形遍历
        res = []
        for i in sorted(dic):
            if i % 2 == 0:
                res.extend(dic[i][::-1])
            else:
                res.extend(dic[i])
        return res