# -*- coding: utf-8 -*-
# @Time    : 2021/3/14 上午8:15
# @Author  : gavin
# @FileName: 59.矩阵中的路径.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩
阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的
某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的
路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子
之后，路径不能再次进入这个格子。

解题方法:
回朔法
注意：回朔过程中要进行还原：　用来进行回溯的，如果当前的节点不满足路径要求，需要撤回到
上一个节点，然而上一个节点此时已经赋值为“/”，需要还原一下，继续探索。
"""


class Solution:

    def exis(self, board, word: str) -> bool:
        """回溯法"""

        def dfs(i, j, k):
            """
            :param i: 行索引
            :param j: 列索引
            :param k: 当前查找元素
            :return:  bool
            """

            # 越界或不满足条件直接返回
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            # 访问结束
            if k == len(word) - 1: return True
            # 标记已访问的路径
            board[i][j] = ""
            res = dfs(i + 1, j, k+1) or dfs(i - 1, j, k+1) or dfs(i, j + 1, k+1) or dfs(i, j - 1, k+1)
            # 回退已访问标记
            board[i][j] = word[k]
            return res

        # 　寻找出口
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True

        return False
