# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 上午9:23
# @Author  : gavin
# @FileName: 38.矩形覆盖.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
"""


class Solution:

    def rectCover(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        return self.rectCover(n - 1) + self.rectCover(n - 2)


if __name__ == "__main__":
    print(Solution().rectCover(4))
