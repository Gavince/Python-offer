# -*- coding: utf-8 -*-
# @Time    : 2022/1/3 上午9:45
# @Author  : gavin
# @FileName: 177.括号生成.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

解题方法：
DFS
时间复杂度：O()
空间复杂度：O()

原题链接：https://leetcode-cn.com/problems/generate-parentheses/
"""


class Solution:

    def generateParenthsis(self, n: int):
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            # 左括号少于括号对数，
            if left > n or right > left: return
            if len(paths) == n * 2:
                res.append(paths)
                return
            dfs(paths + "(", left + 1, right)
            dfs(paths + ")", left, right + 1)

        dfs("", 0, 0)

        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.generateParenthsis(2))
