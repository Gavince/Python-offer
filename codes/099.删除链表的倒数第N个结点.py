# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 上午9:37
# @Author  : gavin
# @FileName: 99.删除链表的倒数第N个结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

示例：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

解题方法：
双指针
时间复杂度:O(N) former指针实现一趟扫描
空间复杂度:O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(0, head)
        former, latter = head, dummy
        # 寻找K
        for i in range(n):
            if not former: break
            former = former.next
        while former:
            latter = latter.next
            former = former.next

        # 删除结点
        latter.next = latter.next.next

        return dummy.next