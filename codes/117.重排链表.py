# -*- coding: utf-8 -*-
# @Time    : 2021/7/30 上午10:59
# @Author  : gavin
# @FileName: 117.重排链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个单链表 L 的头节点 head ，单链表 L 表示为：L0→ L1→ … → Ln-1→ Ln请
将其重新排列后变为：L0→Ln→L1→Ln-1→L2→Ln-2→ …不能只是单纯的改变节点内部的值，而
是需要实际的进行节点交换。

解题方法：
快慢指针 + 链表翻转 + 合并链表

时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/reorder-list/
"""


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 快慢指针拆分

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        # 逆转链表
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 连接
        l1, l2 = head, pre
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
