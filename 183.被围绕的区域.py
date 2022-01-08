# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 上午10:45
# @Author  : gavin
# @FileName: 182.被围绕的区域.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的
区域，并将这些区域里所有的 'O' 用 'X' 填充。

解题方法：
边界点后DFS/BFS的点不存在填充
时间复杂度：O(M*N)
空间复杂度：O(M*N)

原题链接：https://leetcode-cn.com/problems/surrounded-regions/
"""


class Solution:
    def solveOfBFS(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y):

            if not 0 <= x < m or not 0 <= y < n or board[x][y] != "O":
                return
            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)

        # 遍历所有边界，寻找可能的入口
        # 行遍历
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        # 列遍历
        for j in range(n - 1):
            dfs(0, j)
            dfs(m - 1, j)
        # 修改表示
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def solveOfBFS(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def bfs(x, y):

            deque = [(x, y)]
            while deque:
                [x, y] = deque.pop(0)
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    board[x][y] = "A"
                    deque += [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]

        # 遍历所有边界，寻找可能的入口
        # 行遍历
        for i in range(m):
            bfs(i, 0)
            bfs(i, n -1)
        # 列遍历
        for j in range(n - 1):
            bfs(0, j)
            bfs(m - 1, j)
        # 修改表示
        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"