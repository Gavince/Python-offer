# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 下午5:03
# @Author  : gavin
# @FileName: 97.回文链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    请判断一个链表是否为回文链表。进阶：你能否用 O(n) 时间复
杂度和 O(1) 空间复杂度解决此题？

示例：
输入: head = [1,2,3,3,2,1]
输出: true

解题方法：
（1）遍历（判断正向和反向结果是否一致）
使用有个临时数组对遍历节点数值进行存储，并比较
时间复杂度：O(n) 遍历所有节点
空间复杂度：O(n) 临时数组
（2）快慢指针
使用快慢指针寻找链表的中心位置，将链表进行分割l1和l2,并且已证明
l1链表的长度始终大于等于l2链表的长度，因此将l2链表进行翻转与l1
链表进行比较。
时间复杂度：O(n) 遍历所有节点
空间复杂度：O(1) 没有使用额外空间

注意：
此题与链表翻转和排序链表知识点相同, 此外，只有一个节点时，链表是回文的。

原题链接：https://leetcode-cn.com/problems/aMhZSa/
"""


class Solution:

    def isPalindrom1(self, head):
        # 临时数组进行存储
        vars = []
        cur = head
        while cur:
            vars.append(cur.val)
            cur = cur.next

        return vars == vars[::-1]

    def isPalindrom2(self, head):

        if not head or not head.next:
            return True
        # 快慢指针
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow.next
        slow.next = None
        pre = None
        # 链表翻转
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 比较回文
        while pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next

        return True