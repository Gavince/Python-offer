# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 上午8:06
# @Author  : gavin
# @FileName: 25.从上往下打印二叉树 二叉树的广度遍历.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
从上往下打印出二叉树的每个节点，同层节点从左至右打印

解决方案：
简单的层序遍历

原题链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
"""
from typing import List


class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.root = None

    def add_node(self, val):

        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.left is None:
                temp_node.left = node
                return
            else:
                queue.append(temp_node.left)
            if temp_node.right is None:
                temp_node.right = node
                return
            else:
                queue.append(temp_node.right)

        return

    def PrintFromTopToBottom(self, root) -> List[int]:

        if root is None:
            return []
        queue = [root]
        ret = []
        while queue:
            temp_node = queue.pop(0)
            ret.append(temp_node.val)
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        return ret


if __name__ == "__main__":
    obj = Solution()
    for i in range(1, 9):
        obj.add_node(i)
    # print(obj.PrintFromTopToBottom(obj.root))  # [1, 2, 3, 4, 5, 6, 7, 8]
    print(obj.FindPath(obj.root, 15))