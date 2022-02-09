# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 上午7:59
# @Author  : gavin
# @FileName: 20.求第n个丑数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

首先从丑数的定义我们知道，一个丑数的因子只有2,3,5，那么丑数p = 2 ^ x * 3 ^ y * 5 ^ z，
换句话说一个丑数一定由另一个丑数乘以2或者乘以3或者乘以5得到，那么我们从1开始乘以2,3,5，
就得到2,3,5三个丑数，在从这三个丑数出发乘以2,3,5就得到4，6,10,6，9,15,10,15,25九个丑数，
我们发现这种方法会得到重复的丑数，而且我们题目要求第N个丑数，这样的方法得到的丑数也是无序的

解决方案:
方法1:
[丑数](https://blog.csdn.net/ggdhs/article/details/90313512)
方法2:
下一个丑数，一定是由之前某一个丑数乘以2或者乘以3或者是乘以5中的最小值
"""


class Solution:

    def GetUglyNumber_Solution(self, index: int):
        """求取第n个丑数"""
        if index == 0:
            return 0

        # 维护一个有序的丑数数组
        array = [1]
        Q2 = []
        Q3 = []
        Q5 = []
        i = 0
        while i < index:
            Q2.append(array[i] * 2)
            Q3.append(array[i] * 3)
            Q5.append(array[i] * 5)
            minval = min(Q2[0], Q3[0], Q5[0])
            array.append(minval)
            #  保证两个连续相等的值被删除
            if minval == Q2[0]:
                Q2.remove(minval)
            if minval == Q3[0]:
                Q3.remove(minval)
            if minval == Q5[0]:
                Q5.remove(minval)
            i += 1
        return array[i - 1]

    def GetUglyNumber_Solution1(self, index: int):
        """动态调整"""

        if index == 0:
            return 0
        res = [1]
        n2, n3, n5 = 0, 0, 0  # 记录相乘位置
        i = 0
        while i < index:
            val = min(res[n2] * 2, res[n3] * 3, res[n5] * 5)
            res.append(val)
            # 动态更新自己相乘的位置
            if res[n2] * 2 == val:
                n2 += 1
            if res[n3] * 3 == val:
                n3 += 1
            if res[n5] * 5 == val:
                n5 += 1
            i += 1
        return res[i - 1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.GetUglyNumber_Solution(7))
    print(obj.GetUglyNumber_Solution1(7))
