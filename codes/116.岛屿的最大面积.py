# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 上午9:49
# @Author  : gavin
# @FileName: 116.岛屿的最大面积.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个包含了一些 0 和 1 的非空二维数组grid 。一个岛屿是由一些相邻的1(代表土地) 构成
的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设grid的四个边缘都被
0（代表水）包围着。找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0 )

解题方法：
DFS和BFS

原题链接：https://leetcode-cn.com/problems/ZL6zAn/
"""


class Solution:

    def maxAreaOfIslandOfDFS(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j):

            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                return 0
            # 已访问标记
            grid[i][j] = 0
            return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = max(ans, dfs(grid, i, j))

        return ans

    def maxAreaOfIslandOfBFS(self, grid: List[List[int]]) -> int:

        def bfs(grid, i, j):

            deque = [[i, j]]
            count = 0
            while deque:
                [i, j] = deque.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                    # 已访问标记
                    grid[i][j] = 0
                    count += 1
                    deque += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]

            return count

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = max(ans, bfs(grid, i, j))
        return ans
