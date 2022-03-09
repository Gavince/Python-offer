# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 下午3:55
# @Author  : gavin
# @FileName: 124.编辑距离.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述:
	给你两个单词word1 和word2，请你计算出将word1转换成word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符
解题方法:
动态规划
1.状态定义，dp[i][j]表示word1[:i]到word2[:j]的最小编辑距离
2.起始状态，dp[0][i] = 0, dp[j][0] = 0表示空字符编辑
3.状态转移
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
4.返回值，dp[m][n]

附录：对各个状态的理解
对“dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。”的补充理解：
以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为word2的
前 3 个字符，也就是将 horse 转换为 ros，因此有：
(1) dp[i-1][j-1]，即先将 ord1的前4个字符hors转换为word2的前2个字符ro，然后将第五个字符
word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）;
(2) dp[i][j-1]，即先将word1的前5个字符horse转换为word2的前2个字符ro，然后在末尾补充一个s，即插入
操作;
(3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1
的第5个字符.

时间复杂度：O(m*n)
空间复杂度：O(m*n)


原题链接：https://leetcode-cn.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        if n * m == 0:
            return m + n

        # 状态定义
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 起始状态
        # 第一列
        for i in range(m + 1):
            dp[i][0] = i
        # 第一行
        for j in range(n + 1):
            dp[0][j] = j
        # 状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        # 返回值
        return dp[m][n]