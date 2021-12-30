# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 下午4:57
# @Author  : gavin
# @FileName: 78.两数相加.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
并且每个节点只能存储一位数字。请你将两个数相加，并以相同形式返回一个表示和的
链表。你可以假设除了数字 0 之外，这两个数都不会以 0开头。

解题方法：
进位计算

复杂度：
时间复杂度:O(max(L1, L2))
空间复杂度O(1)

注意：
每个节点只能存储一位数值
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 申请头结点
        dummy = cur = ListNode(0)
        # 进位节点
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # 存储节点值
            sum = x + y + carry
            cur.next = ListNode(sum % 10)
            carry = sum // 10
            cur = cur.next
            # 更新节点
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry: cur.next = ListNode(carry)

        return dummy.next
