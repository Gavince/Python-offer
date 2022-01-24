# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 上午10:35
# @Author  : gavin
# @FileName: 187.腐蚀的橘子.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
在给定的网格中，每个单元格可以有以下三个值之一：
值0代表空单元格；
值1代表新鲜橘子；
值2代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回-1。

解题方法：
BFS
提前终止的问题：没有腐烂的橘子和没有新鲜的橘子
1
时间复杂度：O(mn)
空间复杂度：O(mn)

原题链接：https://leetcode-cn.com/problems/rotting-oranges/
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid: return -1
        m, n = len(grid), len(grid[0])
        deque = []
        time = 0  # 标识腐蚀的时间
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # 待腐蚀的橘子队列
                    deque.append([i, j, time])
        # BFS腐蚀橘子
        while deque:
            i, j, time = deque.pop(0)
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x = di + i
                y = dj + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    deque.append([x, y, time + 1])
        # 判断无法腐蚀的情况
        for row in grid:
            if 1 in row:
                return -1
        return time


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    obj = Solution()
    print(obj.orangesRotting(grid))
