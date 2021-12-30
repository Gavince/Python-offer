# -*- coding: utf-8 -*-
# @Time    : 2021/10/31 下午7:28
# @Author  : gavin
# @FileName: 161.旋转链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述:
    给你一个链表的头节点head，旋转链表，将链表每个节点向右移动k个位置。

实例：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

解题方法：
快满指针
时间复杂度：O(N)
空间复杂度：O(1)
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if k == 0 or not head or not head.next:
            return head
        # 统计链表长度
        cur = head
        node_lens = 1
        while cur.next:
            cur = cur.next
            node_lens += 1
        k = k % node_lens

        # 快慢指针
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 循环链接
        fast.next = head
        head = slow.next
        slow.next = None

        return head
