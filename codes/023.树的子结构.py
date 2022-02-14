# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 上午8:30
# @Author  : gavin
# @FileName: 23.树的子结构.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不
是任意一个树的子结构）

解题方法：
DFS
①如果A,B有一个为空，return False
②如果A,B不为空，A.val == B.val, 且B为单节点，则return True;如果结点B不为单节点则需要比较
A.left.val == B.left.val 和 A.right.val == B.right.val
③如果B.val != A.val 则遍历Ａ结点的子节点和B进行比较，找到相同结点后，转②，否则return False

原题链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
"""


class Solution:

    def isSubstructure(self, A, B):

        # A,B 不都为空
        if not A or not B:
            return False

        # 先序遍历，寻找子结构
        return self.isInclude(A, B) or self.isSubstructure(A.left, B) or self.isSubstructure(A.right, B)

    def isInclude(self, A, B):

        # B优先遍历完，且为子结构
        if not B:
            return True
        #　A优先遍历完，且不存在子结构
        if not A or A.val != B.val:
            return False
        # 递归寻找匹配
        return self.isInclude(A.left, B.left) and self.isInclude(A.right, B.right)
