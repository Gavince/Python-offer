# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 上午10:45
# @Author  : gavin
# @FileName: 201.课程表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    现在你总共有 numCourses 门课需要选，记为0到numCourses - 1。给你一个
数组prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课
程 ai 前 必须 先选修bi 。例如，想要学习课程 0 ，你需要先完成课程1 ，我们用
一个匹配来表示：[0,1] 。返回你为了学完所有课程所安排的学习顺序。可能会有多个
正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空
数组 。

解题方法：
拓扑排序:BFS、DFS
时间复杂度：O(M+N)
空间复杂度：O(M+N)

原题链接：https://leetcode-cn.com/problems/course-schedule-ii/
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 标记入度
        indegrees = [0 for _ in range(numCourses)]
        # 标记邻接表
        adjacency = [[] for _ in range(numCourses)]
        deque = []
        result = []
        # 记录结点的入度和邻接边
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # 不需要先修的课程入队列
        for i in range(len(indegrees)):
            if not indegrees[i]:
                deque.append(i)
        # BFS进行遍历
        while deque:
            pre = deque.pop(0)
            result.append(pre)
            numCourses -= 1
            # 先修课程完成
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: deque.append(cur)

        return result if not numCourses else []