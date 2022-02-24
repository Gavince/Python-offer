# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 上午8:25
# @Author  : gavin
# @FileName: 70.删除链表的节点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
解题方法：
单链表的遍历

时间复杂度：o(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
"""

class Solution:

    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        # 头结点满足
        if head.val == val: return head.next

        # 遍历寻找指定结点
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre = cur
            cur = cur.next
        if cur:
            pre.next = cur.next

        return head
