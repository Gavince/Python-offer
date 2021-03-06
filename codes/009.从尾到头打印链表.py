# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 下午9:14
# @Author  : gavin
# @FileName: 9.从尾到头打印链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    输入一个链表，按链表从尾到头的顺序返回一个ArrayList

解决方案：
1. 使用列表存储结点，并翻转
2. 栈
3. 递归(推荐)
fun(node.next) + [node.val]
[] + [8] + [7] + [5]
[8, 7, 5]

原题链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""


class Solution:

    def PrintListFromTailToHeadfor0(self, listNode):
        if not listNode:
            return []

        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next

        result.reverse()

        return result

    def PrintListFromTailToHeadfor1(self, listNode):

        if not listNode:
            return []

        stack = []  # 栈
        result = []

        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        while stack:
            result.append(stack.pop())

        return result

    def PrintListFromTailToHeadfor2(self, listNode):
        if not listNode:
            return []

        return self.PrintListFromTailToHeadfor2(listNode.next) + [listNode.val]
