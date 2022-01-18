# 剑指Offer-回朔法题目总结

[toc]

## 矩阵中的路径（<font color = red>重点</font>）

题目类型：字符串、回朔法

题目难度：:star2::star2::star2:

- 问题描述

  ```python
  问题描述：
          设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串
  所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵
  中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么
  该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符
  串“bfce”的（路径中的字母用"| |"标出）。
   
  [["a","|b|","c","e"],
  ["s","|f|","|c|","s"],
  ["a","d","|e|","e"]]
  
  但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据
  了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
  
  解题方法:
  回朔法
  
  注意：
  1. 回朔过程中要进行还原：用来进行回溯的，如果当前的节点不满足路径要求，
  需要撤回到上一个节点，然而上一个节点此时已经赋值为“/”，需要还原一下，
  继续探索。（打标记和撤标记）。
  2. 起始点为任意一格(需要寻找入口)，且每次只能移动一格数据。
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/))

  图解：

  ![](/home/gavin/Python/剑指offer/总结/imgs/59.png)

  ```python
  class Solution:
  
      def exis(self, board, word: str) -> bool:
          """回溯法"""
  
          def dfs(i, j, k):
              """
              :param i: 行索引
              :param j: 列索引
              :param k: 当前查找元素
              :return:  bool
              """
  
              # 越界或不满足条件直接返回
              if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
              if k == len(word) - 1: return True
              # 标记已访问的路径
              board[i][j] = ""
              # 下上右左进行访问
              res = dfs(i + 1, j, k+1) or dfs(i - 1, j, k+1) or dfs(i, j + 1, k+1) or dfs(i, j - 1, k+1)
              board[i][j] = word[k]
              
              return res
  
          # 寻找入口
          for i in range(len(board)):
              for j in range(len(board[0])):
                  if dfs(i, j, 0): return True
  
          return False
  ```

## 机器人的运动范围（<font color = red>重点</font>）

题目类型：DFS、BFS

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人
  从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移
  动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当
  k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格
  [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
  
  解题方法：
  DFS和BFS
  时间复杂度:O(MN)
  空间复杂度:O(MN)
  注意条件：
  1.不能越界
  2.满足行列坐标位数和要求(不能大于的格子里面)
  3.机器人起始点为[0, 0]（区别与上一题中的任意入口）
  4. 19, 20 or 1, 2 两种情况
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/)）

  数位和公式

  ```python
  def sums(self, x):
      """位数和"""
  
      s = 0
      while x != 0:
          s += x % 10  # 求余数，得低位置
          x = x // 10  # 去低位
      return s
  ```

  **DFS**

  ```python
  class Solution:
  
      def movingCount(self, m: int, n: int, k, int) -> int:
  
          def dfs(i, j, si, sj):
              
              # 越界条件
              if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
              visited.add((i, j))
              # 先下后右
              return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) \
                     + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
              
          # 设置已访问标记
         visited = set()
          return dfs(0, 0, 0, 0)
  ```

  **BFS**

  ```python
  class Solution:
      def movingCount(self, m: int, n: int, k: int) -> int:
  
          queue = [(0, 0, 0, 0)]
          visited = set()
          while queue:
              i, j, si, sj = queue.pop(0)
              if i >= m or j >= n or k < si + sj or (i, j) in visited: 
                  continue
              visited.add((i, j))
              queue.append((i + 1, j, si + 1 if (i + 1)%10 else si - 8, sj))
              queue.append((i, j + 1, si, sj + 1 if (j + 1)%10 else sj - 8))
          
          return len(visited)
  ```

## 岛屿数量（<font color = red>重点</font>）

题目类型：DFS、BFS

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述:
          给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿
  的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻
  的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。
  
  解题方法：
  DFS 和　BFS
  ```

- 代码

  DFS
  
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
  ```
  
  **BFS**
  
  ```python
  class Solution:
      
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

## 岛屿的最大面积（<font color = red>重点</font>）

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

  

