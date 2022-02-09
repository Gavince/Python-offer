# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 下午8:38
# @Author  : gavin
# @FileName: 17.删除链表中重复的结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的
结点不保留，返回链表头指针。

解决方案：
当删除重复结点时，直接遍历重复结点后，跳跃连接一前一后的结点
前：１->1->2->3->4->5->6->6
后：2->3->4->5

时间复杂度：O(N)
空间复杂度：O(1)
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def deleteDuplication(self, head):
        # 申请新的头结点
        if head is None: return head
        dummy = cur = ListNode(0, head)

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

    def deleteDuplication1(self, pHead):
        """递归实现"""

        if pHead is None:
            return None
        if pHead.next is None:
            return pHead
        if pHead.val != pHead.next.val:
            pHead.next = self.deleteDuplication1(pHead.next)
            return pHead
        else:
            # 设置临时结点，用来删除重复数值
            tempNode = pHead
            while tempNode and tempNode.val == pHead.val:
                tempNode = tempNode.next
            return self.deleteDuplication1(tempNode)

    def show(self, pHead):

        if pHead is None:
            return None

        while pHead:
            print(pHead.val, end=" ")
            pHead = pHead.next


if __name__ == "__main__":
    obj = Solution()
    # 创建数据
    n1 = ListNode(2)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(5)
    n5 = ListNode(6)
    n1.next = n2  # 依次将结点链接起来，形成一个链表
    n2.next = n3
    n3.next = n4
    n4.next = n5
    p = n1
    obj.show(p)
    print("\n")
    obj.show(obj.deleteDuplication1(n1))
    print("\n")
    obj.show(obj.deleteDuplication1(n1))
