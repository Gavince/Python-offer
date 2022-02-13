# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 下午9:36
# @Author  : gavin
# @FileName: 10.链表中倒数第k个结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入一个链表，输出该链表中倒数第k个结点

解决方案：
方法1：使用栈存储，先进后出。
方法2：双指针(双指针相差k，先前指针走完时，正好后指针到指定结点)
 former + after = after + former
 K + M = Ｍ + K
 时间复杂度:O(N)
 空间复杂度：O(1)
 原题链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
"""


class Solution:

    def FindKthToTail(self, head, k):
        """双指针，两个指针之间相差k值"""

        former, latter = head, head
        for _ in range(k):
            if not former: return None
            former = former.next

        while former:
            former = former.next
            latter = latter.next

        return latter

