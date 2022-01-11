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
时间复杂度：O(mn)
空间复杂度：O(mn)

原题链接：https://leetcode-cn.com/problems/rotting-oranges/
"""


class Solution:
    def orangesRotting(self, grid) -> int:

        m, n = len(grid), len(grid[0])
        # 标记腐烂橘子的位置
        time = 0
        deque = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    deque.append((i, j, time))

        # 开始腐烂新鲜橘子
        while deque:
            i, j, time = deque.pop(0)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    deque.append((i + di, j + dj, time + 1))
        # 无法腐蚀的橘子
        for row in grid:
            if 1 in row: return -1

        return time


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    obj = Solution()
    print(obj.orangesRotting(grid))
