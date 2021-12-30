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
构建最小堆，进行堆排序
时间复杂度：O(NlogN)
空间复杂度：O()
"""
import heapq


class Solution:
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