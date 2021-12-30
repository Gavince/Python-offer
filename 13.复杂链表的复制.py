# -*- coding: utf-8 -*-
# @Time    : 2020/8/16 下午9:21
# @Author  : gavin
# @FileName: 13.复杂链表的复制.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，**一个指向下一个节点，另一个特殊指针指向任意一个节点**），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空。

解决方案：
A---  a***  --->B  ***>b
A.next.random = a.random.next
"""


class RandomListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, phead: 'Node') -> 'Node':

        if phead is None:
            return None

        # 复制结点
        cur = phead
        while cur:
            tmpNode = RandomListNode(cur.val)
            tmpNode.next = cur.next
            cur.next = tmpNode
            cur = tmpNode.next

        # 随机指针复制
        cur = phead
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 拆分结点
        cur = res = phead.next
        pre = phead

        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        # pre.next =None

        return res












