# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 下午9:07
# @Author  : gavin
# @FileName: 163.两数相加II.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储
一位数字。将这两数相加会返回一个新的链表。你可以假设除了数字0之外，这两个数字都不会以零开
头。

实例:
输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]

解题方法：
链表头插法
时间复杂度：O(max(M, N))
空间复杂度：O(M + N)

原题链接：https://leetcode-cn.com/problems/add-two-numbers-ii/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 申请两个栈
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        dummy = ListNode(0)
        carry = 0
        while stack1 or stack2 or carry:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            sum_ = x + y + carry
            carry = sum_ // 10
            # 头插法
            cur = ListNode(sum_ % 10)
            cur.next = dummy.next
            dummy.next = cur

        return dummy.next