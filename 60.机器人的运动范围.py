# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 上午8:15
# @Author  : gavin
# @FileName: 60.机器人的运动范围.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格
子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐
标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=
18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

解题方法：
回朔法

注意条件：
1.不能越界
2.满足行列坐标位数和要求
3.机器人起始点为[0, 0]
"""


class Solution:

    def movingCount(self, m: int, n: int, k, int) -> int:

        def dfs(i, j, si, sj):
            # 越界条件
            if i >= m or j >= n or k > si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            # 先下后右
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) \
                   + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        # 设置已访问标记
        visited = set()
        return dfs(0, 0, 0, 0)

    def sums(self, x):
        """位数和"""

        s = 0
        while x != 0:
            s += x % 10
            x = x // 10
        return s


if __name__ == "__main__":
    obj = Solution()
    print(obj.sums(444))
