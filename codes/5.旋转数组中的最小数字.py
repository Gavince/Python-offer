# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 下午4:59
# @Author  : gavin
# @FileName: 5.旋转数组中的最小数字.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
	把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输
入一个非减排序的数组的一个旋转，输旋转数组的最小元素。例如数组{3,4,5,1,2}为
{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若
数组大小为0，请返回0

解决方案:
1. 暴力搜索
2. 分治法
分治法是不断的缩小范围,从而找到符合条件的解
二分法的分析我们知道,数组可以分为前后两个递增数组,下面的分析也都利用递增的特性
(1) 当numbers[mid] > numbers[high]时,说明最小值在mid的右边,缩小范围low = mid + 1
(2) 当numbers[mid] == numbers[high]时,我们不知道最小值的范围,但是可以肯定的是去除
numbers[high]是没有影响的,缩小范围high -= 1
(3) 当numbers[mid] < numbers[high]时,我们知道最小值的不是numbers[mid]就是在mid
的左边,缩小范围high = mid

时间复杂度：O(logN)
空间复杂度：O(1)

测试用例： 51234, 34512, 22222
"""


class Solution:

    def minArray(self, numbers):
        """旋转数组最小值"""

        # 二分法
        # 三种情况
        # 51234, 34512, 22222
        if not numbers:
            return None
        low = 0
        high = len(numbers) - 1
        while low < high:
            mid = (low + high) >> 1
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] == numbers[high]:
                high -= 1
            else:
                high = mid
        return numbers[low]
