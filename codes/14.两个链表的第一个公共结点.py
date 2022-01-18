# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 下午8:50
# @Author  : gavin
# @FileName: 14.两个链表的第一个公共结点.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
输入两个链表，找出它们的第一个公共节点。

解决方案：
1. 暴力搜索
No Recommend
2.使用栈从后向前找出第一个不相等的结点
A:1 2 5 6
公共结点---->10 11 55 88
B:2 4 8 9
3. 交替遍历指针
时间复杂度：（M + N）
空间复杂度：（１）
p1 -> --->......p1=p2
p2 --> ---->......return p1
实例：
a:(1 2 3 4 ) 10 10 10
b:(0 7 8 9 6 5 2)  10 10 10
c(公共部分): 10 10 10
a + c + b = b + c + a

时间复杂度：O(a + b)
空间复杂度：O(1)
"""


class Solution:

    def findFirstCommonNode(self, pHead1, pHead2):
        """烂漫相遇问题（我走过你来时的路）"""

        node1, node2 = pHead1, pHead2

        while node1 != node2:
            node1 = node1.next if node1 else pHead2
            node2 = node2.next if node2 else pHead1

        return node1
