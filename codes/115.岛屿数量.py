# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 下午9:43
# @Author  : gavin
# @FileName: 115.岛屿数量.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿
的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆
地连接形成。此外，你可以假设该网格的四条边均被水包围。

解题方法：
DFS和BFS

原题链接：https://leetcode-cn.com/problems/number-of-islands/
"""
from typing import List


class Solution:

    def numIslandsOfDFS(self, grid: List[List[str]]) -> int:

        def dfs(grid, i, j):

            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            # 上下左右进入节点
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        count = 0
        # 寻找入口
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1

        return count

    def numIslandsOfBFS(self, grid: List[List[str]]) -> int:

        def bfs(grid, i, j):

            deque = [[i, j]]
            while deque:
                [i, j] = deque.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                    grid[i][j] = "0"
                    deque += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0": continue
                bfs(grid, i, j)
                count += 1
        return count
