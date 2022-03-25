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
（1）递归（有重复计算项）
时间复杂度：O(N^2)
空间复杂度：O(N)

（2）递归（保留重复计算项）
时间复杂度：O(N)
空间复杂度：O(N)

（3）动态规划（时间复杂度O(n), 空间复杂度O(1)）
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
斐波那契数列——普通递归、记忆化搜索、动态规划:https://blog.csdn.net/qq_42032507/article/details/104446541?utm_term=%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97%E8%AE%B0%E5%BF%86%E5%8C%96%E9%80%92%E5%BD%92&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-1-104446541&spm=3001.4430
"""


class Solution:

    def fibonacci(self, n):
        """递归算法(时间复杂度极高O(n)=２^n)"""
        if n == 1 or n == 2:
            return 1

        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fib0(self, n: int) -> int:
        """记忆花递归"""
        memo = [-1] * (n + 1)

        def dfs(n):
            if n == 0: return 0
            if n == 1: return 1
            if memo[n] == -1:
                memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n) % 1000000007

    def fib1(self, n: int) -> int:
        """动态规划"""

        if n == 0: return 0
        if n == 1: return 1
        # 定义转态
        dp = [0] * (n + 1)
        # 初始化转态
        dp[0], dp[1] = 0, 1
        # 转态转移
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        # 返回值
        return dp[n] % 1000000007

    def fib2(self, n: int) -> int:
        """优化的动态规划"""

        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a


if __name__ == "__main__":
    obj = Solution()
    print("F1:", obj.fibonacci(10))
    print("F2:", obj.fibonacci1(10))
    print("F3:", obj.fibonacci2(10))
