# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 下午6:36
# @Author  : gavin
# @FileName: 173.用Rand7()实现Rand10().py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    已有方法rand7可生成 1 到 7 范围内的均匀随机整数，试写一个方法rand10生成 1 到 10 范围
内的均匀随机整数。不要使用系统的Math.random()方法。

解题方法：
要利用rand7()实现rand10()
第 1 步： 我们根据推导结论，利用rand7()方法来随机选取 7 * 7 矩阵中的某个元素
计算表达式为：(rand7() - 1) * 7 + rand7()
第 2 步： 判断选出的元素是否属于前 40 个，如果不是需要返回第 1 步重新选取元素
第 3 步： 若该属于前 40 个，但是直接输出的话超出 [1,10] 的范围，该怎么处理呢？

时间复杂度：O(1)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7/
"""


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            col = rand7()
            row = rand7()
            index = (col - 1)*7 + row
            if index <= 40:
                return (index - 1)%10 + 1