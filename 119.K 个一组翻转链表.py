# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 下午10:10
# @Author  : gavin
# @FileName: 119.K个一组翻转链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。如果节点总数不是k的
整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

解题方法：
时间复杂度：O(N)
空间复杂度：O(N)
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        cur = head
        count = 0
        while cur and count < k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                nxt = head.next
                head.next = cur
                cur = head
                head = nxt
                count -= 1
            head = cur
        return head