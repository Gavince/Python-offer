# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 下午5:29
# @Author  : gavin
# @FileName: 107.前K个高频元素.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
你可以按 任意顺序 返回答案。

实例：
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
"""
from typing import List
from collections import defaultdict
from collections import Counter
import heapq

class Solution:

    def topKFrequent1(self, nums, k):
        """直接排序"""

        count = Counter(nums)
        return [item[0] for item in count.most_common(k)]

    def topkFrequent(self, nums, k):
        """堆排序"""

        count = Counter(nums)
        hp = [(val, key) for key, val in count.items()]
        return [item[1] for item in heapq.nlargest(k, hp)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """字典计数"""
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

        for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]:
            res.append(key)

        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.topKFrequent1(nums=[1, 2, 2, 5, 4, 4, 4, 4, 6], k=2))
