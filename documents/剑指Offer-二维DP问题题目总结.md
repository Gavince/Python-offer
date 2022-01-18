# 剑指Offer-二维DP问题题目总结

[toc]

## 礼物的最大值（<font color = red>重点</font>）

题目类型：动态规划

题目难度：:star2::star2:

此题有最大值和最小值两种类型，并且要注意==每种题型每次所走的路径方向==。

### 最大值（leetcode）

- 问题描述

  ```
  问题描述：
  	在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值
  大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一
  格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能
  拿到多少价值的礼物？
  
  实例：
  [[1,3,1],
    [1,5,1],
    [4,2,1]]
  输出: 12
  解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
  
  解题方法：
  动态规划
  转态定义：dp[i]][j]表示当前位置礼物的最大值；
  转态转移：dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])；
  初始值：dp[0][j] += dp[0][j - 1], dp[i][0] += dp[i - 1][0], 第一行和第一列的值只能从左和上
  方过度过来；
  返回值：dp[-1][-1]。
  
  复杂度:
  时间复杂度：O(M*N)
  空间复杂度：O(1)
  
  注意：
  (1)入口为左上角,出口为右下角
  (2)每次向下或向右移动一格
  ```

- 代码（[解题思路](https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5vr32s/)）

  ![](./imgs/63.png)

  ```python
  class Solution:
      def maxValue(self, grid: List[List[int]]) -> int:
  
          m, n = len(grid), len(grid[0])
  
          # 起始转态(第一行)
          for j in range(1, n):
              grid[0][j] += grid[0][j - 1]
          
          # 起始状态（第一列）
          for i in range(1, m):
              grid[i][0] += grid[i-1][0]
          
          # 转移方程(向左 向上)
          for i in range(1, m):
              for j in range(1, n):
                  grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
                  
          # 返回值
          return grid[-1][-1]
  ```

### 最小值：牛妹的的礼物（牛客网）

- 问题描述

  ```
  问题描述：
  	众所周知，牛妹有很多很多粉丝，粉丝送了很多很多礼物给牛妹，牛妹的礼物摆满了地板。
  地板是N×M的格子，每个格子有且只有一个礼物，牛妹已知每个礼物的体积。地板的坐标是左
  上角(1,1)  右下角（N, M）。牛妹只想要从屋子左上角走到右下角，每次走一步，每步只能向下
  走一步或者向右走一步或者向右下走一步每次走过一个格子，拿起（并且必须拿上）这个格子上
  的礼物。牛妹想知道，她能走到最后拿起的所有礼物体积最小和是多少？
  
  解题方法：
  转态定义：dp[i]][j]表示当前位置礼物的最小值；
  初始值：dp[0][j] += dp[0][j - 1], dp[i][0] += dp[i - 1][0]；
  转态转移：dp[i][j] = min(dp[i-1][j-1],，dp[i][j-1]，dp[i-1][j])) + presentVolumn[i][j]；
  返回值：dp[-1][-1]。
  
  复杂度:
  时间复杂度O(M*N)
  空间复杂度O(1)
  
  注意：
  (1)入口为左上角,出口为右下角
  (2)每次向下或向右或向右下角移动一格
  ```

- 代码

  ```python
  class Solution:
      def selectPresent(self , presentVolumn ):
   
          m, n = len(presentVolumn), len(presentVolumn[0])       
          # 初始化第一行
          for j in range(1, n):
              presentVolumn[0][j] += presentVolumn[0][j - 1]
          # 初始化第一列
          for i in range(1, m):
              presentVolumn[i][0] += presentVolumn[i - 1][0]
              
          # 遍历所有节点(上，左，左上)
          for i in range(1, m):
              for j in range(1, n):
                  presentVolumn[i][j] += min(presentVolumn[i-1][j], presentVolumn[i][j-1], presentVolumn[i-1][j-1])
          
          return presentVolumn[-1][-1]
  ```

## 编辑距离

题目类型：字符串、动态规划

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述:
  	给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
  你可以对一个单词进行如下三种操作：
  
  - 插入一个字符
  - 删除一个字符
  - 替换一个字符
  解题方法:
  
  动态规划
  1.状态定义，dp[i][j]表示word1[:i]到word2[:j]的最小编辑距离
  2.起始状态，dp[0][i] = 0, dp[j][0] = 0表示空字符编辑
  3.状态转移
  
                  if word1[i - 1] == word2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1]
                  else:
                      dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                      
  4.返回值，dp[m][n]
  
  时间复杂度：O(m*n)
  空间复杂度：O(m*n)
  ```

- 代码

  ```python
  class Solution:
      def minDistance(self, word1: str, word2: str) -> int:
  
          m, n = len(word1), len(word2)
          
          if n * m == 0:
              return m + n
  
          # 状态定义
          dp = [[0]*(n + 1) for _ in range(m + 1)]
          # 起始状态
          # 第一列
          for i in range(m + 1):
              dp[i][0] = i
          # 第一行
          for j in range(n + 1):
              dp[0][j] = j
          # 状态转移
          for i in range(1, m + 1):
               for j in range(1, n + 1):
                  if word1[i - 1] == word2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1]
                  else:
                      dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
          # 返回值
          return dp[m][n]
  ```

## 不同路径I（<font color = red>重点</font>）

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
  (3) 转态转移：dp[i][j] = dp[i][j - 1] + dp[i - 1][j] 遇见障碍 continue
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

## 最长公共子序列（<font color = red>重点</font>）

题目类型：字符串、动态规划

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 
  公共子序列 ，返回 0 。一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变
  字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
  
  例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
  两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
  
  解题方法：
  动态规划
  1.状态定义，dp[i][j]表示text1[:i]和text2[:j]最长的公共子序列
  2.起始状态，dp[0][i] = 0, dp[j][0] = 0表示空字符和任何字符串的公共子序列长度为0
  3.状态转移
                  if text1[i - 1] == text2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1] + 1
                  else:
                      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
  4.返回值，dp[m][n]
  
  时间复杂度：O(m*n)
  空间复杂度：O(m*n)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/longest-common-subsequence/solution/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/)）

  算法图解

  <img src="/home/gavin/Python/剑指offer/总结/imgs/123.png" style="zoom: 80%;" />

  ```python
  class Solution:
      def longestCommonSubsequence(self, text1: str, text2: str) -> int:
  
          m, n = len(text1), len(text2)
          # 状态定义和起始值
          dp = [[0]*(n + 1) for _ in range(m + 1)]
          # 状态转移
          for i in range(1, m + 1):
              for j in range(1, n + 1):
                  if text1[i - 1] == text2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1] + 1
                  else:
                      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                      
          return dp[m][n] 
  ```

- 相似题目（最长重复子数组）

  ==注意：子数组不连续、子数组不连续、子数组不连续==

  ```
  问题描述：
  	给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
  示例：
  输入：
  A: [1,2,3,2,1]
  B: [3,2,1,4,7]
  输出：3
  解释：
  长度最长的公共子数组是 [3, 2, 1] 。注意每一次的更新只能从左上角进行更新
  ```

- 代码

- 算法图解

  <img src="/home/gavin/Python/剑指offer/总结/imgs/123_2.png" style="zoom:80%;" />

- ```python
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
          # 返回值
          return ans  
  ```


## 最小路径和（<font color = red>重点</font>）

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

  