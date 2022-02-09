# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 上午9:40
# @Author  : gavin
# @FileName: 32.按之字形顺序打印二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右
到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

示例：
例如:
给定二叉树: [3,9,20,null,null,15,7]
[
  [3],
  [20,9],
  [15,7]
]

解题方法：
层序遍历

原题链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
"""

import collections


class Solution:

    def levelOrder(self, root):

        if not root: return []
        res, deque = [], collections.deque([root])

        while deque:

            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val)
                else: tmp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))

        return res
