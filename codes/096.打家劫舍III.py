# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 上午10:03
# @Author  : gavin
# @FileName: 96.打家劫舍III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区
只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个
直接相连的房子在同一天晚上被打劫，房屋将自动报警。计算在不触动警报的情况下，小偷一晚
能够盗取的最高金额。

解题方法：
树型动态规划(后序遍历)
1. 转态定义： dp = [val1, val2] 下标0表示为不偷， 下标1表示为偷
2. 状态转移： 如果当前节点能被偷，则有val2 = cur.val + left[0] + right[0]
否则如果当前节点不能偷，则有val1 = max(left[0], left[1]) + max(right[0], right[0])
3. 初始状态： dp = [0, 0]
4. 返回值: max(dp[0], dp[1])
时时间复杂度：O(n)
空间复杂度：O()
"""


class TreeNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:

    def rob(self, cur: TreeNode) -> int:
        def dfs(cur):
            if not cur:
                return [0, 0]

            left = dfs(cur.left)
            right = dfs(cur.right)

            # 状态转移
            # 当前节点不可偷
            val1 = max(left[0], left[1]) + max(right[0], right[1])
            # 当前节点可偷
            val2 = cur.val + left[0] + right[0]
            return [val1, val2]

        res = dfs(cur)
        return max(res[0], res[1])
