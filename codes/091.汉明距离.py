# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 下午9:46
# @Author  : gavin
# @FileName: 91.汉明距离.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

解题方法：
两步走原则：
（1）通过异或操作统计bit1的不相同位（异或操作取不同）
11:1011
8:1000
^:0011

（2）通过x & (x - 1) 统计bit1的出现次数(转换为比特位计数)
step1:
x = 3 -->0011
(x - 1) = 2 -->0010
step2:
x = 2 -->0010
(x - 1) = 1 -->0001
step3:
x = 1 -->0001
(x - 1) = 0 -->0000
step4:
终止：x = 0 -->0000

时间复杂度：(logC)，其中 C 是元素的数据范围，在本题中logC=log2^31 = 31
空间复杂度：O(1)。

知识点：
与：遇0得0
运算规则：0&0=0; 0&1=0; 1&0=0; 1&1=1;
或：遇1得1
运算规则：0|0=0； 0|1=1； 1|0=1； 1|1=1；
异或：相同为0，不同为1
运算规则：0^0=0； 0^1=1； 1^0=1； 1^1=0

原题链接：https://leetcode-cn.com/problems/hamming-distance/
基础题型-位1的个数：https://leetcode-cn.com/problems/number-of-1-bits/
进阶题目-汉明总距离：https://leetcode-cn.com/problems/total-hamming-distance/
"""


class Solution:

    def hammingWeight(self, n: int) -> int:
        """计算1的个数"""
        ans = 0
        while n:
            n = n & (n - 1)
            ans += 1

        return ans

    def hammingDistance(self, x: int, y: int) -> int:
        """计算两个数值之间的汉明距离"""

        res, cnt = x ^ y, 0
        while res:
            res &= (res - 1)
            cnt += 1

        return cnt
