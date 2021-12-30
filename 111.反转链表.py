# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 上午10:26
# @Author  : gavin
# @FileName: 111.反转链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你单链表的头指针 head 和两个整数left和right ，其中left <= right。请你反转从位置 eft到位
置 right 的链表节点，返回 反转后的链表。

示例：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

解题方法：
穿针引线
时间复杂度：O(N)
空间复杂度:O(1)
"""


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if not head: return None
        dummy = pre = ListNode(0, head)
        cnt = 1
        # 寻找左边界
        while pre and cnt < left:
            pre = pre.next
            cnt += 1
        cur = pre.next
        tail = cur
        # 连接
        while cur and cnt <= right:
            nxt = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = nxt
            tail.next = cur
            cnt += 1
        return dummy.next
