# -*- coding: utf-8 -*-
# @Time    : 2020/9/15 上午8:38
# @Author  : gavin
# @FileName: 29.数据流中的中位数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之
后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平
均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数.

"""
import heapq


class Solution:

    def __init__(self):
        """初始化最大最小堆"""

        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        """添加元素"""

        # 相等保证最小堆个数大于最大堆
        # 最大堆－>最小堆　　—>最大堆
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]


if __name__ == "__main__":
    obj = Solution()
    obj.addNum(2)
    obj.addNum(3)
    print(obj.findMedian())