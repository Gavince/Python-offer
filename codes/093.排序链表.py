# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 上午9:10
# @Author  : gavin
# @FileName: 93.排序链表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你链表的头结点head，请将其按 升序 排列并返回 排序后的链表 。
进阶：你可以在O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进
行排序吗？

示例：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

解题方法：
归并排序
时间复杂度：O(nlogn)
空间复杂度：O(n)

原题链接：https://leetcode-cn.com/problems/7WHec2/
"""


# 分治排序
def mergeSort(arr):
    if len(arr) < 2:
        return arr

    middle = (len(arr)) // 2
    left, right = arr[:middle], arr[middle:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    """
    有序合并
    :param left:左有序
    :param right: 右有序
    :return: 有序合并
    """
    result = []
    while left and right:
        # 比较插入
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # 填补剩余部分
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result


# 链表排序
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """合并排序"""
        # 只有一个节点时，各子部分有序
        if not head or not head.next:
            return head
        # 查找二分有的右节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        return self.merge(self.sortList(head), self.sortList(head2))

    def merge(self, head1, head2):
        # 创建临时借点
        dummy = pre = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                pre.next = head1
                head1 = head1.next
            else:
                pre.next = head2
                head2 = head2.next
            pre = pre.next
        # 添加剩余节点
        pre.next = head1 if head1 else head2

        return dummy.next


if __name__ == "__main__":
    nums = [1, 2, 9, 3, 4, 6, 5, 10]
    print(mergeSort(nums))
