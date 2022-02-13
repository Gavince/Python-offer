# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 下午8:51
# @Author  : gavin
# @FileName: 0.斐波那契数列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
	写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐
波那契数列的定义如下： 0 1 1 2 3 5 8 13　... F(n) = F(n-1) + F(n-2) (n > 2)斐波那契数列
由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。答案需要取模 1e9+7
（1000000007），如计算初始结果为：1000000008，请返回 1。

解题方法：
（1）递归（有重复计算项, 时间复杂度O(2^n)）
（2）动态规划（时间复杂度O(n), 空间复杂度O(1)）
状态定义：设 dp 为一维数组，其中dp[i] 的值代表斐波那契数列第 i 个数字 。
转移方程：dp[i+1]=dp[i]+dp[i−1] ，即对应数列定义 f(n+1)=f(n)+f(n−1) ；
初始状态：dp[0]=0, dp[1] = 1 ，即初始化前两个数字；
返回值：dp[n]，即斐波那契数列的第 n 个数字。

实际处理过程中，并不需要存储每一个dp状态的数值，因此：
模拟运算
i=0 1 2 3 4 5
0 1 1 2 3 5
a b
  a b
    a b
      a b
        a b
          a b

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
"""


class Solution:

    def fibonacci(self, n):
        """递归算法(时间复杂度极高O(n)=２^n)"""
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        if n > 2:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci1(self, n):
        """动态规划问题"""

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            a = 1  # 较大值
            b = 0  # 较小值
            ret = 0
            for i in range(2, n + 1):  # 左闭右开
                ret = a + b
                b = a
                a = ret

            return ret

    def fibonacci2(self, n):
        """列表写法O(n)=n"""

        if n == 0:
            return 0
        if n == 1:
            return 1
        result = [0, 1]
        for i in range(2, n + 1):
            result.append(result[i - 1] + result[i - 2])

        return result[-1]

    def fib(self, n: int) -> int:

        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a

if __name__ == "__main__":
    obj = Solution()
    print("F1:", obj.fibonacci(10))
    print("F2:", obj.fibonacci1(10))
    print("F3:", obj.fibonacci2(10))
