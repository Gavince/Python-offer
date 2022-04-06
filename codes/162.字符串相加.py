# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 下午8:03
# @Author  : gavin
# @FileName: 162.字符串相加.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符
串转换为整数形式。

解题方法：
双指针
时间复杂度：O(max(m, n))
空间复杂度：O(1)

原题链接：https://leetcode-cn.com/problems/add-strings/
相似题目（二进制的加法）：https://leetcode-cn.com/problems/JFETK5/
相似题目（两数相加）：https://leetcode-cn.com/problems/add-two-numbers/
"""


class ListNode:

    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            # 求解进位
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1

        return "1" + res if carry else res

    def addBinary(self, a: str, b: str) -> str:

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            cur_val = x + y + carry
            carry = cur_val // 2
            res = str(cur_val % 2) + res
            i -= 1
            j -= 1

        return "1" + res if carry else res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            cur_sum = x + y + carry
            cur.next = ListNode(cur_sum % 10)
            cur = cur.next
            carry = cur_sum // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        cur.next = ListNode(carry) if carry else None

        return dummy.next
