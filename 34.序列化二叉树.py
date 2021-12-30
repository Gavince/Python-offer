# -*- coding: utf-8 -*-
# @Time    : 2021/2/9 上午10:04
# @Author  : gavin
# @FileName: 34.序列化二叉树.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
请实现两个函数，分别用来序列化和反序列化二叉树
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序
、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
"""
import collections


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def serialize(self, root):
        """序列化二叉树"""
        if not root: return "[]"
        res, queue = [], collections.deque(root)

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"

    def deserilize(self, data):
        """将序列化后的二叉树，解码为原二叉树"""
        if data == "[]": return None
        vals, i = data[1:-1].split(","), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1

        return root
