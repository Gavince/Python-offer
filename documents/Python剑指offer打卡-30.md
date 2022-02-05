# Python剑指offer打卡-30

[toc]

## 寻找两个正序数组的中位数

题目类型：数组

题目难度：:star2:

- 问题描述

  ```
  5问题描述：
      给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请
  你找出并返回这两个正序数组的 中位数 。
  
  解题方法：
  归并排序的归并阶段
  时间复杂度：O(m + n)
  空间复杂度：O(m + n)
  ```

- 代码

  ```python
  class Solution:
      def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
  
          res = self.merge(nums1, nums2)
          # 奇数
          mid = len(res) // 2
          if len(res) % 2:
              return res[mid]
          else:
              return (res[mid - 1] + res[mid]) / 2
  
      def merge(self, arr1, arr2):
  
          result = []
          i, j = 0, 0
  
          while i < len(arr1) and j < len(arr2):
              if arr1[i] < arr2[j]:
                  result.append(arr1[i])
                  i += 1
              else:
                  result.append(arr2[j])
                  j += 1
          result += arr1[i:]
          result += arr2[j:]
  
          return result
  ```

## 汉明总距离

题目类型：位运算

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      两个整数汉明距离 指的是这两个数字的二进制数对应位不同的数量。给你一个
  整数数组 nums，请你计算并返回 nums 中任意两个数之间汉明距离的总和。
  
  解题方法：
  位操作算法
  ```

- 代码

  ```python
  class Solution:
      def totalHammingDistance(self, nums: List[int]) -> int:
          ans = 0
          n = len(nums)
  
          for i in range(30):
              c = sum([((val >> i) & 1) for val in nums])
              ans += c * (n - c)
  
          return ans
  ```
  

## 不同路径（<font color = red>重点</font>）

题目类型：动态规划

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。机器人每
  次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
  问总共有多少条不同的路径？
  
  解题方法：
  动态规划
  (1) 定义状态：dp[i][j]表示到达i, j的不同路径
  (2) 初始值：dp[0][j] = 1, dp[i][0] = 1
  (3) 转态转移：　dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
  (4) 返回值：dp[-1][-1]
  时间复杂度：O(n*m)
  空间复杂度：O(m*n)
  ```

- 代码

  ```python
  class Solution:
      def uniquePaths(self, m: int, n: int) -> int:
  
          # 定义转态
          dp = [[0] * n for _ in range(m)]
          # 初始转态
          for i in range(m):
              dp[i][0] = 1
          for j in range(n):
              dp[0][j] = 1
  
          # 转态转移
          for i in range(1, m):
              for j in range(1, n):
                  dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
  
          # 返回值
          return dp[-1][-1]
  ```
  

## 路径总和（<font color = red>重点</font>）

题目类型：DFS、BFS

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你二叉树的根节点root 和一个表示目标和的整数targetSum ，判断该树中是否存在 根节点到叶子节点
  的路径，这条路径上所有节点值相加等于目标和targetSum 。叶子节点 是指没有子节点的节点。
  
  解题方法：
  DFS和BFS
  ```

- 代码

  ```python
  import collections
  
  
  class Solution:
      def hasPathSumOfDFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
  
          if root is None:
              return False
  
          if root.left is None and root.right is None:
              return targetSum == root.val
  
          return self.hasPathSumOfDFS(root.left, targetSum - root.val) \
                 or self.hasPathSumOfDFS(root.right, targetSum - root.val)
  
  
      def hasPathSumOfBFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
  
          if root is None:
              return False
  
          deque = collections.deque([(root, root.val)])
          while deque:
  
              root, path = deque.popleft()
              if not root.left and not root.right and targetSum == path:
                  return True
  
              if root.left:
                  deque.append((root.left, root.left.val + path))
              if root.right:
                  deque.append((root.right, root.right.val + path))
  
          return False
  ```
  

## 数组中重复的数据

题目类型：数组

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
  找到所有出现两次的元素。你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
  
  解题方法：
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def findDuplicates(self, nums: List[int]) -> List[int]:
  
          if not nums: return []
  
          res = []
          n = len(nums)
          for i in range(n):
              num = abs(nums[i])
              if nums[num - 1] < 0:
                  res.append(num)
              else:
                  nums[num - 1] = -nums[num - 1]
          return res
  ```
  





  

