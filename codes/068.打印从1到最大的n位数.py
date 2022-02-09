# -*- coding: utf-8 -*-
# @Time    : 2021/5/7 上午8:59
# @Author  : gavin
# @FileName: 68.打印从1到最大的n位数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3
一直到最大的 3 位数 999。

实例:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9

解题方法：

"""


class Solution:

    def printNumbers(self, n: int):

        return list(range(1, 10 ** n))

    def printNumbersMethod1(self, n: int):
        """
        从1至最大的n位数的列表
        :return 00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20
        """

        def dfs(x):
            # 出口
            if x == n:
                res.append("".join(nums))
                return
            # 访问下一个位置
            for i in range(10):
                nums[x] = str(i)
                dfs(x + 1)  # 固定下一位置

        nums = ["0"]*n
        res = []
        dfs(0)

        return ",".join(res)

    def printNumbersMethod2(self, n: int):
        """
        使用大数定理
        :param n: n位数
        :return: 列表结果
        """
        def dfs(x):
            if x == n:
                # 去除除高位以的零值
                s = ".".join(nums[self.satrt:])
                # 去除第一位是"0"的可能
                if s != "0": res.append(int(s))
                # 进位(逢九进位)
                if n - self.satrt == self.nine:
                    self.satrt -= 1
                return
            # 遍历每一位的可能取值
            for i in range(10):
                if i == 9: self.nine += 1
                nums[x] = str(i)
                dfs(x + 1)
            # 归置
            self.nine -= 1


        res, nums = [], ["0"]*n
        self.nine = 0
        self.satrt = n - 1
        dfs(0)
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.printNumbersMethod1(2))


