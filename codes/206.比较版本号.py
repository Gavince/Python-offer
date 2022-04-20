# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 上午7:49
# @Author  : gavin
# @FileName: 206.比较版本号.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给你两个版本号 version1 和 version2 ，请你比较它们。版本号由一个或多个修订号组成，各修订号由一个 '.'
连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0
开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。比较
版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，
修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版
本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。
返回规则如下：
如果version1>version2返回1，
如果version1<version2 返回 -1，
除此之外返回 0

示例1:
输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"

示例２：
输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"

解题方法：
双指针模拟比较
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/compare-version-numbers/solution/
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        m, n = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            # 每次只比较相邻修订号之间的数值大小
            a, b = 0, 0
            while i < m and version1[i] != ".":
                a = 10 * a + int(version1[i])
                i += 1
            while j < n and version2[j] != ".":
                b = b * 10 + int(version2[j])
                j += 1
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                # 　跳过当前修订号位置
                i += 1
                j += 1
        return 0