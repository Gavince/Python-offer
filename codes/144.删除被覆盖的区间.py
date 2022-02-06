# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 下午5:13
# @Author  : gavin
# @FileName: 144.删除被覆盖的区间.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。只有当c <= a
且b <= d时，我们才认为区间[a,b) 被区间[c,d) 覆盖。在完成所有删除
操作后，请你返回列表中剩余区间的数目。

解题方法：
排序 + 遍历
排序遵循：左端从小到大，右端从大到小

时间复杂度：O(NlogN)，其中N是区间的个数。
空间复杂度：O(logN)，为排序需要的空间。

原题链接：https://leetcode-cn.com/problems/remove-covered-intervals/
"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        # 先按照
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, r_max = len(intervals), intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= r_max:
                ans -= 1
            else:
                r_max = max(r_max, intervals[i][1])

        return ans