# Python剑指offer打卡-31

[toc]

## 分发糖果（<font color = red>重点</font>）

题目类型：双指针

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      老师想给孩子们分发糖果，有 N个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
  你需要按照以下要求，帮助老师给这些孩子分发糖果：每个孩子至少分配到 1 个糖果。评分更高的孩子必须
  比他两侧的邻位孩子获得更多的糖果。那么这样下来，老师至少需要准备多少颗糖果呢？
  
  解题方法：
  双指针
  时间复杂度：O(N)
  空间复杂度：O(N)
  ```

- 代码

  ```python 
  class Solution:
      def candy(self, ratings: List[int]) -> int:
  
          left = [1 for _ in range(len(ratings))]
          right = left[:]
          # 左遍历
          for i in range(1, len(ratings)):
              if ratings[i] > ratings[i - 1]:
                  left[i] = left[i - 1] + 1
          cnt = left[-1]
  
          # 右遍历
          for i in range(len(ratings) - 2, -1, -1):
              if ratings[i] > ratings[i + 1]:
                  right[i] = right[i + 1] + 1
  
              cnt += max(left[i], right[i])
  
          return cnt
  
  ```


## 验证二叉搜索树

题目类型：树

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
  给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
  
  解题方法：
  BFS和DFS
  ```

- 代码

  ```python
  class Solution1:
      def isValidBST(self, root: TreeNode) -> bool:
  
          if root is None: False
  
          deque = []
          cur = root
          pre_val = float("-inf")
          while deque or cur:
              while cur:
                  deque.append(cur)
                  cur = cur.left
  
              node = deque.pop()
              if node.val <= pre_val:
                  return False
              pre_val = node.val
              cur = node.right
  
          return True
  
  class Solution2:
      def __init__(self):
          self.pre = float('-inf')
      def isValidBST(self, root: TreeNode) -> bool:
          if root is None: return True
          if not self.isValidBST(root.left): return False
          if root.val <= self.pre:  return False
          self.pre = root.val
          return self.isValidBST(root.right)
  ```

## 最长重复子数组（<font color = red>重点</font>）

题目类型：动态规划

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
  
  解题思路：
  动态规划
  dp[i][j]代表以A[i-1]与B[j-1]结尾的公共字串的长度,公共字串必须以A[i-1]，B[j-1]结束，
  即当A[i-1] == B[j-1]时，dp[i][j] = dp[i-1][j-1] + 1; 当A[i-1] != B[j-1]时，
  以A[i-1]和B[j-1]结尾的公共字串长度为0,dp[i][j] = 0。输出最大的公共字串的长度即为最
  长重复字串。
  时间复杂度：O(M*N)
  空间复杂度：O(M*N)
  注意：
  记住，子序列默认不连续，子数组默认连续
  ```

- 代码

  ```python
  class Solution:
      def findLength(self, nums1: List[int], nums2: List[int]) -> int:
  
          m, n = len(nums1), len(nums2)
  
          # 定义状态和起始值
          dp = [[0]*(n + 1) for _ in range(m + 1)]
          ans = 0
  
          # 状态转移
          for i in range(1, m + 1):
              for j in range(1, n + 1):
                  if nums1[i - 1] == nums2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1] + 1
                      ans = max(ans, dp[i][j])
          return ans
  ```

## 不同路径II（<font color = red>重点</font>）

题目类型：动态规划

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      一个机器人位于一个 m x n 网格的左上角（起始点在下图中标记为“Start” ）。
  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为
  “Finish”）。现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路
  径？网格中的障碍物和空位置分别用1和0来表示。
  
  解题方法：
  动态规划
  (1) 定义状态：dp[i][j]表示到达i, j的不同路径
  (2) 初始值：dp[0][j] = 1, dp[i][0] = 1，遇见障碍 break
  (3) 转态转移：　dp[i][j] = dp[i][j - 1] + dp[i - 1][j] 遇见障碍 continue
  (4) 返回值：dp[-1][-1]
  时间复杂度：O(n*m)
  空间复杂度：O(m*n)
  ```

- 代码

  ```python
  class Solution:
      def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
  
          # 定义dp
          m, n = len(obstacleGrid), len(obstacleGrid[0])
          dp = [[0] * n for _ in range(m)]
          # 定义初始转态
          # 有障碍区进行跳转
          for i in range(m):
              if obstacleGrid[i][0]: break
              dp[i][0] = 1
          for j in range(n):
              if obstacleGrid[0][j]: break
              dp[0][j] = 1
  
          # 转态转移
          for i in range(1, m):
              for j in range(1, n):
                  if obstacleGrid[i][j] == 1: continue
                  dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
          # 返回值
          return dp[m - 1][n - 1]
  ```

## 搜索旋转排序数组（<font color = red>重点</font>）

题目类型：二分法

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      整数数组 nums 按升序排列，数组中的值 互不相同 。在传递给函数之前，nums 在预先未知的某个下标
  k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1],
  nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标
  3 处经旋转后可能变为[4,5,6,7,0,1,2] 。给你 旋转后 的数组 nums 和一个整数 target ，如果
  nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。
  
  
  解题方法：
  二分法
  时间复杂度：O(logn)
  空间复杂度：O(1)
  ```

- 二分法代码

  ```python
  class Solution:
      def search(self, nums: List[int], target: int) -> int:
  
          
          low, high = 0, len(nums) - 1
  
          while low <= high:
              mid = (low + high) // 2
  
              if nums[mid] > target:
                  high = mid - 1
              elif nums[mid] < target:
                  low = mid + 1
              else:
                  return mid
          
          return -1
  ```
  
- 代码

  ```python
  class Solution:
      def search(self, nums: List[int], target: int) -> int:
  
          if not nums: return -1
  
          l, r = 0, len(nums) - 1
          while l <= r:
  
              mid = (l + r) // 2
              if nums[mid] == target:
                  return mid
              if nums[0] <= nums[mid]:
                  if nums[0] <= target < nums[mid]:
                      r = mid - 1
                  else:
                      l = mid + 1
              else:
                  if nums[mid] < target <= nums[-1]:
                      l = mid + 1
                  else:
                      r = mid - 1
          return -1
  ```



