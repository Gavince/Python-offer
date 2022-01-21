# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 上午9:54
# @Author  : gavin
# @FileName: 200.课程表I.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。在选修某些课程
之前需要一些先修课程。 先修课程按数组prerequisites 给出，其中prerequisites[i] =
[ai, bi] ，表示如果要学习课程ai 则 必须 先学习课程 bi 。例如，先修课程对[0, 1] 表
示：想要学习课程 0 ，你需要先完成课程 1 。请你判断是否可能完成所有课程的学习？如果可以，
返回 true ；否则，返回 false 。

解题方法：
拓扑排序:DFS、BFS
时间复杂度：O(M + N)
空间复杂度：O(M + N)

原题链接：https://leetcode-cn.com/problems/course-schedule/
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 标记入度
        indegrees = [0 for _ in range(numCourses)]
        # 标记邻接表
        adjacency = [[] for _ in range(numCourses)]
        deque = []

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
            numCourses -= 1
            # 先修课程完成
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: deque.append(cur)

        return not numCourses