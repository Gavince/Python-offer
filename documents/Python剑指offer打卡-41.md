# Python剑指offer打卡-41

[toc]

## 矩阵中的最长递增路径

题目类型：DFS

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
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
  ```
  
- 代码

  ```python
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
  ```
  
## N叉树的最大深度

题目类型：DFS+BFS

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个 N 叉树，找到其最大深度。最大深度是指从根节点到最远叶子节点
  的最长路径上的节点总数。N叉树输入按层序遍历序列化表示，每组子节点由空值
  分隔（请参见示例）。
  
  解题方法：
  BFS和DFS
  
  原题链接：https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/solution/n-cha-shu-de-zui-da-shen-du-by-leetcode-n7qtv/
  ```
  
- 代码

  ```python
  class Solution:
      def maxDepthforBFS(self, root: 'Node') -> int:
  
          if root is None:
              return 0
          deque = [root]
          ans = 0
          while deque:
              deque = [child for node in deque for child in node.children]
              ans += 1
          return ans
  
      def maxDepthforDFS(self, root: 'Node') -> int:
          if not root:
              return 0
          if not root.children:
              return 1
  
          return max(self.maxDepthforDFS(child) + 1 for child in root.children)
  ```
  
## 链表的中间结点

题目类型：链表

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个头结点为 head 的非空单链表，返回链表的中间结点。如果有
  两个中间结点，则返回第二个中间结点。
  
  示例：
  输入：[1,2,3,4,5]
  输出：此列表中的结点 3 (序列化形式：[3,4,5])
  返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
  注意，我们返回了一个 ListNode 类型的对象 ans，这样：
  ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以
  及 ans.next.next.next = NULL.
  
  解题方法：
  快慢指针
  时间复杂度：O(N)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/
  ```

- 代码

  ```python
  class Solution:
      def middleNode(self, head: ListNode) -> ListNode:
  
          if not head or not head.next:
              return head
  
          slow, fast = head, head.next
          while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
  
          return slow.next if fast else slow
  ```
## 汉明总距离

题目类型：位运算

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      两个整数的汉明距离 指的是这两个数字的二进制数对应位不同的数量。给你一个整
  数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。
  
  示例：
  输入：nums = [4,14,2]
  输出：6
  解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为
  了体现后四位之间关系）
  所以答案为：
  HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6
  
  解题方法：
  4: 0100
  14:1110
  2: 0010
  -------
  统计每一位置上1的个数
  (vall>>i)&1
  2*1 + 1*2 + 2*1 = 6
  时间复杂度：O(n*L)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/total-hamming-distance/
  ```

- 代码

  ```python
  class Solution:
      def totalHammingDistance(self, nums: List[int]) -> int:
  
          ans, n = 0, len(nums)
          for i in range(30):
              # 计算同一个位置上的“１”数值
              c = sum([(val >> i) & 1 for val in nums])
              ans += c * (n - c)
  
          return ans
  ```

## 搜索排序数组

题目类型：DFS+记忆化

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多
  次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。
  注意: 若有多个相同元素，返回索引值最小的一个。
  
  
  示例：
  输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],
  target = 5
  输出: 8（元素5在该数组中的索引）
  
  解题方法：
  二分法
  时间复杂度：O(logN)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/search-rotate-array-lcci/
  ```
  
- 代码

  ```python
  class Solution:
      def search(self, arr: List[int], target: int) -> int:
          # 二分法算法下进行部分有序查找
          if not arr: return -1
          left, right = 0, len(arr) - 1
          while left <= right:
              # 1 1 1 2 1 target:1
              if arr[left] == target:
                  return left
              mid = (left + right) // 2
              # 1 2 2 1 1 target:2
              if arr[mid] == target:
                  right = mid
              # 1 2 3 4 5 target:2
              elif arr[0] < arr[mid]:
                  if arr[0] <= target < arr[mid]:
                      right = mid - 1
                  else:
                      left = mid + 1
              # 4 5 1 2 3 target:2
              elif arr[0] > arr[mid]:
                  if arr[mid] < target <= arr[-1]:
                      left = mid + 1
                  else:
                      right = mid - 1
              # 1 1 1 1 2 1 target:2
              else:
                  left += 1
          return -1
  ```

