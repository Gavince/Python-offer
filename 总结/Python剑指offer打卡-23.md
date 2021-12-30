# Python剑指offer打卡-23

[toc]

## 反转链表II（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你单链表的头指针 head 和两个整数left和right ，其中left <= right。请你反转从位置 eft到位
  置 right 的链表节点，返回 反转后的链表。
  
  示例：
  输入：head = [1,2,3,4,5], left = 2, right = 4
  输出：[1,4,3,2,5]
  
  解题方法：
  穿针引线
  时间复杂度：O(N)
  空间复杂度:O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/dong-hua-tu-jie-fan-zhuan-lian-biao-de-z-n4px/)）

  算法图解：

  ![](./imgs/111.png)

  ```python
  class Solution:
  
      def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
  
          # 申请哑节点
          dummmy = ListNode(0)
          dummmy.next = head
          # 记录
          count = 1
          pre = dummmy
          # 找到开头节点
          while pre.next and count < left:
              pre = pre.next
              count += 1
  
          cur = pre.next
          tail = cur
          # 局部翻转
          while cur and count <= right:
              nxt = cur.next
              # 节点插入连接
              cur.next = pre.next
              pre.next = cur
              # tail节点始终未变，只有指向在变换
              tail.next = nxt
              # 移动
              cur = nxt
              count += 1
  
          return dummmy.next
  ```

## 数组中的第K个最大元素（<font color = red>重点</font>）

题目类型：数组

题目难度：:star2::star2::star2:

- 问题描述

  ```
  题目描述：
          给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。请注意，
  你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
  
  解题方法：
  改进的快速排序
  	思想：基本的快速排序选取第一个或者最后一个元素作为基准。这样在数组已
  经有序的情况下，每次划分将得到最坏的结果。一种比较常见的优化方法是随机化
  算法，即随机选取一个元素作为基准。这种情况下虽然最坏情况仍然是O(n2)，但最
  坏情况不再依赖于输入数据，而是由于随机函数取值不佳。实际上，随机化快速排
  序得到理论最坏情况的可能性仅为1/(2n)。所以随机化快速排序可以对于绝大多数
  输入数据达到O(nlogn)的期望时间复杂度。
  时间复杂度：O(NlogN)
  空间复杂度：O(1)
  ```

- 代码

  快速排序

  ```python
  class Solution:
      def findKthLargest(self, nums: List[int], k: int) -> int:
  
          def quickSort(low, high):
              if low >= high:
                  return 
              
              # 设置边界条件
              i, j = low, high
              pivot = nums[i]
              while i < j:
                  while i < j and nums[j] >= pivot:
                      j -= 1
                  nums[i] = nums[j]
                  
                  while i < j and nums[i] < pivot:
                      i += 1
                  nums[j] = nums[i]
              nums[i] = pivot
              quickSort(low, i - 1)
              quickSort(i + 1, high)
          
          quickSort(0, len(nums) - 1)
  
          return nums[-k]
  ```

  改进的快速排序

  ```python
  import random
  
  
  class Solution:
      def findKthLargest(self, nums: List[int], k: int) -> int:
  
          def quickSort(nums, start, end):
  
              if start >= end:
                  return 
              
              # 随机初始化基准
              low, high = start, end
              index = random.randint(low, high)
              nums[low], nums[index] = nums[index], nums[low]
              pivot = nums[low]
  
              while low < high:
                  while low < high and nums[high] >= pivot:
                      high -= 1
                  nums[low] = nums[high]
                  while low < high and nums[low] < pivot:
                      low += 1
                  nums[high] = nums[low]
              # 置换
              nums[low] = pivot
              
              # 节省不必要的分裂开支
              if len(nums) - k < low: 
                  quickSort(nums, start, low - 1)
              else: 
                  quickSort(nums, low + 1, end)
          
          quickSort(nums, 0, len(nums) - 1)
          return nums[len(nums) - k]
  ```

## x的平方根（<font color = red>重点</font>）

题目类型：数字

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
          实现int sqrt(int x)函数。计算并返回x的平方根，其中x 是非负整数。
  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
  
  解题方法：
  (1)袖珍计算器
  时间复杂度：O(1)
  空间复杂度：O(1)
  (2)二分法
  时间复杂度：O(logN)
  空间复杂度：O(1)
  (3)牛顿迭代法
  时间复杂度：O(1)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/)）

  袖珍计算器

  ```python
  import math
  
  
  class Solution:
      def mySqrt(self, x: int) -> int:
          
          if x == 0:
              return 0
          ans = int(math.exp(0.5*math.log(x)))
  
          return ans + 1 if (ans + 1)**2 <= x else ans
  ```

  二分法

  ```python
  class Solution:
      
      def mySqrt(self, x: int) -> int:
          # 二分查找
  
          l, r, ans = 0, x, -1
          while l <= r:
              mid = (l + r) // 2
              if mid * mid <= x:
                  ans = mid
                  l = mid + 1
              else:
                  r = mid - 1
  
          return ans
  ```
  
  牛顿的迭代法(可求得精确解)
  
  ```python
  class Solution:
      def mySqrt(self, x: int) -> int:
  
          if x <= 1:
              return x
          x0, C = float(x), float(x)
          while True:
              xi = 0.5*(x0 + C/x0)
              if abs(xi - x0) < 1e-7:
                  break
              x0 = xi
          return int(x0)
  ```


## 合并两个有序数组

题目类型：数组

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1
  成为一个有序数组。初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1
  的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。
  
  解题方法：
  逆向双指针
  
  时间复杂度：O(m + n)
  空间复杂度:O(1)
  ```

- 代码

  ```python
  class Solution:
      def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
          """
          Do not return anything, modify nums1 in-place instead.
          """
          tail = m + n - 1
  
          while m > 0 and n > 0:
              if nums1[m - 1] > nums2[n - 1]:
                  nums1[tail] = nums1[m - 1]
                  m -= 1
              else:
                  nums1[tail] = nums2[n - 1]
                  n -= 1
              tail -= 1
          nums1[:n] = nums2[:n]
  ```

## 岛屿数量（<font color = red>重点</font>）

题目类型：DFS、BFS

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述:
      给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿
  的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆
  地连接形成。此外，你可以假设该网格的四条边均被水包围。
  
  解题方法：
  DFS 和　BFS
  ```

- 代码

  ```python
  class Solution:
  
      def numIslands_dfs(self, grid: List[List[str]]) -> int:
  
          def dfs(grid, i, j):
  
              if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == "0":
                  return
              grid[i][j] = "0"
              # 上下左右进入节点
              dfs(grid, i + 1, j)
              dfs(grid, i - 1, j)
              dfs(grid, i, j + 1)
              dfs(grid, i, j - 1)
  
          count = 0
          # 寻找入口
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                  if grid[i][j] == "1":
                      dfs(grid, i, j)
                      count += 1
  
          return count
  
      def numIslands_bfs(self, grid: List[List[str]]) -> int:
  
          def bfs(grid, i, j):
  
              deque = [[i, j]]
              while deque:
                  [i, j] = deque.pop(0)
                  if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                      grid[i][j] = "0"
                      deque += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
  
          count = 0
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                  if grid[i][j] == "0": continue
                  bfs(grid, i, j)
                  count += 1
          return count
  ```

  
