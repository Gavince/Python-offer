# Python剑指offer打卡-24

[toc]

## 岛屿的最大面积

题目类型：DFS、BFS

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个包含了一些 0 和 1 的非空二维数组grid 。一个岛屿是由一些相邻的1(代表土地) 构成
  的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设grid的四个边缘都被
  0（代表水）包围着。找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0 )
  
  解题方法：
  DFS和BFS
  ```

- 代码

  **DFS**

  ```python
  class Solution:
      def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  
          def dfs(grid, i, j):
  
              if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                  return 0
              # 已访问标记
              grid[i][j] = 0
              return 1 + dfs(grid, i + 1, j) + dfs(grid, i - 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1)
  
          ans = 0
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                  if grid[i][j]:
                      ans = max(ans, dfs(grid, i, j))
          
          return ans
  ```

  **BFS**

  ```python
  class Solution:
      def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
  
          def bfs(grid, i, j):
              
              deque = [[i, j]]
              count = 0
              while deque:
                  [i, j] = deque.pop(0)
                  if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                      # 已访问标记
                      grid[i][j] = 0
                      count += 1
                      deque += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
              
              return count
  
          ans = 0
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                  if grid[i][j]:
                      ans = max(ans, bfs(grid, i, j))
          return ans
  
  ```

## 重排链表

题目类型：链表

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个单链表 L 的头节点 head ，单链表 L 表示为：L0→ L1→ … → Ln-1→ Ln请
  将其重新排列后变为：L0→Ln→L1→Ln-1→L2→Ln-2→ …不能只是单纯的改变节点内部的值，而
  是需要实际的进行节点交换。
  
  解题方法：
  快慢指针 + 链表翻转 + 合并链表
  
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  快慢指针寻找中间节点（回文链表）

  ![](./imgs/97.png)

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def reorderList(self, head: ListNode) -> None:
          """
          Do not return anything, modify head in-place instead.
          """
          # 快慢指针拆分
          slow, fast = head, head.next
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
          
          cur = slow.next
          slow.next = None
          # 逆转链表
          pre = None
          while cur:
              tmp = cur.next
              cur.next = pre
              pre = cur
              cur = tmp
          # 两个链表的合并
          l1, l2 = head, pre
          while l1 and l2:
              l1_tmp = l1.next
              l2_tmp = l2.next
  
              l1.next = l2
              l1 = l1_tmp
  
              l2.next = l1
              l2 = l2_tmp
  ```


## 有效的括号

题目类型：链表

题目难度：:star2:

- 问题描述

  ```
  问题描述：
      给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
  有效字符串需满足：左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。
  
  解题方法：
  栈
  
  时间复杂度：O(N)
  空间复杂度：O(N)
  ```

- 代码

  ```python
  class Solution:
      def isValid(self, s: str) -> bool:
           #奇数直接返回False
          if len(s) % 2: return False
          # 构建括号对
          dic = {"[":"]", "{": "}", "(": ")", "?": "?"}
          # 配对
          stack = ['?']
  
          for c in s:
              # 左括号进入
              if c in dic:
                  stack.append(c)
              elif dic[stack.pop()] != c:
                  return False
              
          return len(stack) == 1
  ```

## K个一组翻转链表

题目类型：链表

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。k 是
  一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那
  么请将最后剩余的节点保持原有顺序。
  进阶：
  你可以设计一个只使用常数额外空间的算法来解决此问题吗？
  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
  
  解题方法：
  仿照单链表的翻转
  ```

- 代码

  ```python
  class Solution:
      def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
  
          cur = head
          count = 0
          while cur and count < k:
              cur = cur.next
              count += 1
          if count == k:
              cur = self.reverseKGroup(cur, k)
              while count:
                  nxt = head.next
                  head.next = cur
                  cur = head
                  head = nxt
                  count -= 1
              head = cur
          return head
  ```

## 最小路径和

题目类型：动态规划

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述:
      给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得
  路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。
  
  解题方法:
  该题目与礼物的最大值相似,采用动态规划解决
  ```

- 代码

  ```python
  class Solution:
      def minPathSum(self, grid: List[List[int]]) -> int:
  
          # grid[i][j]表示当前路径最小值
          # 初始化
          for i in range(1, len(grid)):
              grid[i][0] += grid[i - 1][0]
  
          for j in range(1, len(grid[0])):
              grid[0][j] += grid[0][j - 1]
  
          # 状态转移,求解最小路径
          for i in range(1, len(grid)):
              for j in range(1, len(grid[0])):
                  grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
  
          # 返回状态
          return grid[-1][-1]
  ```

  
