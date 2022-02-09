# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 上午9:39
# @Author  : gavin
# @FileName: 46.滑动窗口的最大值.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的
 k个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

如：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

解题方法：
单调队列：只需要维护有可能成为窗口里最大值的元素就可以了，同时保证队里里的元素数值是由大到小的。
"""

import collections

from rope.base.builtins import List


class Solution:

    def maxSlidingWindow(self, nums, k: int):
        """
        滑动窗口最大值
        :param num: 数组
        :param k: 窗口大小
        :return: 最大值
        """

        deque = collections.deque()
        res, n = [], len(nums)
        # 共n-k+1个有效窗口
        for i, j in zip(range(1 - k, n - k + 1), range(n)):
            # 左删除
            if i > 0 and deque[0] == nums[i - 1]: deque.popleft()
            # 右添加，保留最大
            while deque and deque[-1] < nums[j]: deque.pop()
            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])

        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxSlidingWindow(nums=[3, 3, 5, 6, 7], k=3))
