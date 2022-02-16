# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 下午10:08
# @Author  : gavin
# @FileName: 203.链表的中间结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个头结点为 head 的非空单链表，返回链表的中间结点。如果有
两个中间结点，则返回第二个中间结点。

示例：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以
及 ans.next.next.next = NULL.

解题方法：
快慢指针ggit
时间复杂度：O(N)
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/
"""


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow.next if fast else slow