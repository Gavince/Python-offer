# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 上午9:19
# @Author  : gavin
# @FileName: 30.二叉树的下一个结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:

    def GetNext(self, pNode):

        if pNode.right:
            tmp_node = pNode.right
            while tmp_node.left:
                tmp_node = tmp_node.left
            return tmp_node
        else:
            tmp_node = pNode
            while tmp_node.next:  # 当前节点为父节点的左节点
                if tmp_node.next.left == tmp_node:
                    return tmp_node.next
                tmp_node = tmp_node.next  # 寻找父结点，当前结点为父节点的右节点
            return None
