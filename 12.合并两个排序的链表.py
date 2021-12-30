# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 下午9:32
# @Author  : gavin
# @FileName: 12.合并两个排序的链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解决方案：
1. 构建一个新的链表用于添加合并后的有序链表
2. 递归
"""


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def merge(pHead1, pHead2):

        if not pHead1 and not pHead2:
            return None

        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        # 构建新的链表
        newnode = ListNode(-1)
        temp = newnode
        p1, p2 = pHead1, pHead1

        while p1 and p2:

            if p1.val < p2.val:
                temp.next = ListNode(p1.val)
                temp = temp.next
                p1 = p1.next
            else:
                temp.next = ListNode(p2.val)
                temp = temp.next
                p2 = p2.next
        # 连接未遍历部分的数据
        if p1:
            temp.next = p1
        if p2:
            temp.next = p2

        return newnode

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        phead, cur = ListNode(0), ListNode(0)
        phead = cur

        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        return phead.nex

