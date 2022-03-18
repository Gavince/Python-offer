# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 下午5:49
# @Author  : gavin
# @FileName: 143.合并k个升序链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合
并到一个升序链表中，返回合并后的链表。

解题方法：
方法一：构建最小堆，进行堆排序
时间复杂度：O(NlogK)
空间复杂度：O(K)

方法二：顺序合并
时间复杂度：O(NKK)
空间复杂度：O(1)

方法三：归并思想
    时间复杂度分析：K 条链表的总结点数是 N，平均每条链表有 N/K 个节点，因此合并两条链
表的时间复杂度是 O(N/K)。从 K 条链表开始两两合并成 1 条链表，因此每条链表都会被合并
logK 次，因此 K 条链表会被合并 K * logK次，因此总共的时间复杂度是 K∗logK∗N/K 即
O（NlogK）。

时间复杂度：O(NKlogK)
空间复杂度：O(logK)

原题链接：https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""
import heapq


class Solution0:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not List:
            return None
        if len(lists) == 1:
            return lists[0]

        dummy = cur = ListNode(-1)
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        # 构建有序链表
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return dummy.next


class Solution１:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        tmp = None
        for cur in lists:
            tmp = self.merge(tmp, cur)

        return tmp

    def merge(self, left, right):

        dummy = cur = ListNode(0)

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        cur.next = left if left else right

        return dummy.next


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists: return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = cur = ListNode(-1)

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        cur.next = left if left else right

        return dummy.next
