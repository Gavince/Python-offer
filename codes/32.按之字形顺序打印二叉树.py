# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 上午9:40
# @Author  : gavin
# @FileName: 32.按之字形顺序打印二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""

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
