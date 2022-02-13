# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 下午9:32
# @Author  : gavin
# @FileName: 12.合并两个排序的链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的
链表满足单调不减规则。

解题方法：
简单遍历
时间复杂度：O(M + N)
空间复杂度：O(1)

原题链接：　https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 申请哑结点
        dummy = cur = ListNode(0)
        # 合并公共部分
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 合并剩余部分
        cur.next = l1 if l1 else l2

        return dummy.next
