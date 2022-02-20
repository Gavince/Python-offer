# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 下午9:11
# @Author  : gavin
# @FileName: 86.合并二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
   　 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一
些节点便会重叠。你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠
，那么将他们的值相加作为节点合并后的新值，否则不为NULL的节点将直接作为新二叉
树的节点。

示例：
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7

输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

解题方法：
两棵二叉树同时先序遍历，需要判断两个节点是否同时存在。
时间复杂度：O(min(m, n))
空间复杂度：O(min(m, n))

注意：
    题目要求此题为覆盖（一个树的覆盖到另一个树上），因此，需要直接在原有二叉
树上进行修改(原地修改)，而另一种情况，需要创建一棵新的二叉树来保存合并后的结果，
两种题型，因此需要注意审清题目。

原题链接：https://leetcode-cn.com/problems/merge-two-binary-trees/
"""


class Solution:

    def mergeTrees1(self, t1, t2):
        """合并二叉树（需要生成新树）"""

        def dfs(t1, t2):
            if not (t1 and t2):
                return t1 if t1 else t2
            # 合并节点
            merge = TreeNode(t1.val + t2.val)
            merge.left = dfs(t1.left, t2.left)
            merge.right = dfs(t1.right, t2.right)
            return merge

        return dfs(t1, t2)

    def mergeTrees2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """不需要创建一颗新树"""

        def dfs(root1, root2):
            if not (root1 and root2):
                return root1 if root1 else root2

            # root1做主，root2做辅
            root1.val = root1.val + root2.val
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            return root1

        return dfs(root1, root2)
