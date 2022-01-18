# Python剑指offer打卡-27

[toc]

## 第N位数

题目类型：字符

题目难度：:star2:

- 问题描述

  ```
  问题描述：
  	在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。
  注意：n 是正数且在 32 位整数范围内（n < 231）。
  
  解题方法：
  时间复杂度：O(N)。
  空间复杂度：O(1)
  ```

- 代码

  算法图解

  ![](./imgs/131.png)

  ```python
  class Solution:
      def findNthDigit(self, n: int) -> int:
  
          n -= 1
          # 遍历可能的位数
          for digit in range(1, 11):
              firsr_num = 10**(digit - 1)
              # 判断查找数字位于第几位数
              if n < 9*digit*firsr_num:
                  # 第几位数的第几个数字的第几位数
                  return int(str(firsr_num + n // digit)[n%digit])
              n -= 9*digit*firsr_num
  ```


## 求根到叶子节点数字之和

题目类型：DFS、BFS

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      	给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0
  到 9 之间的数字。每条从根节点到叶节点的路径都代表一个数字：例如
  ，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。计算从根节点到
  叶节点生成的 所有数字之和 。叶节点是指没有子节点的节点。
  
  解题方法：
  DFS 和BFS
  时间复杂度：O(N)
  空间复杂度：O(N)
  ```

- 代码

  DFS
  
  ```python
  class Solution:
      # DFS
      def sumNumbers(self, root: TreeNode) -> int:
  
          def dfs(root, sum):
  
              if root is None:
                  return 0
              elif root.left is None and root.right is None:
                  return 10 * sum + root.val
  
              return dfs(root.left, 10 * sum + root.val) + dfs(root.right, 10 * sum + root.val)
  
          return dfs(root, 0)
  ```
  
  BFS
  
  ```python
  class Solution:
      # BFS
      def sumNumbers(self, root: TreeNode) -> int:
  
          if not root:
              return 0
  
          total = 0
          node_deque = collections.deque([root])
          val_deque = collections.deque([root.val])
  
          while node_deque:
              node = node_deque.popleft()
              num = val_deque.popleft()
              left, right = node.left, node.right
              # 遍历到叶子节点
              if not left and not right:
                  total += num
              else:
                  # 每一节点存储到当前节点的加和值，并和节点一一对应
                  if left:
                      node_deque.append(left)
                      # 当前值乘以进位（每一层作为一个进位）
                      val_deque.append(num * 10 + left.val)
                  if right:
                      node_deque.append(right)
                      val_deque.append(num * 10 + right.val)
  
          return total
  ```


## 二叉树的中序遍历

题目类型：二叉树、DFS、BFS

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个二叉树的根节点 root ，返回它的 中序 遍历。
  
  解题方法：
  (1)递归
  (2)遍历
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/)）

  递归

  ```python
  class Solution:
      
      def inorderTraversal(self, root: TreeNode) -> List[int]:
          """递归"""
  
          res = []
  
          def dfs(root):
              if root is None:
                  return
  
              dfs(root.left)
              res.append(root.val)
              dfs(root.right)
  
          dfs(root)
          return root
  ```

  非递归

  ```python
  class Solution:
      
      def inorderTraversal(self, root: TreeNode) -> List[int]:
          """非递归"""
  
          res = []
          stack = []
          cur = root
          while stack or cur:
              while cur:
                  stack.append(cur)
                  cur = cur.left
  
              tmp_node = stack.pop()
              res.append(tmp_node.val)
              cur = tmp_node.right
  
          return res
  ```

- 相似题目

  二叉树的先序遍历（根左右）

  ```python
  class Solution:
      def postorderTraversal(self, root: TreeNode) -> List[int]:
  
          stack = []
          res = []
          cur = root
          while stack or cur:
              while cur:
                  res.append(cur.val)
                  stack.append(cur)
                  cur = cur.left
              tmp_node = stack.pop()
              cur = tmp_node.right
          
          return res     
  ```

  二叉树的后序遍历（左右根）

  先根右左进行遍历，然后翻转得到结果。

  ```python
  class Solution:
      def postorderTraversal(self, root: TreeNode) -> List[int]:
  
          stack = []
          res = []
          cur = root
          while stack or cur:
              while cur:
                  res.append(cur.val)
                  stack.append(cur)
                  cur = cur.right
              tmp_node = stack.pop()
              cur = tmp_node.left
          
          return res[::-1]
  ```

## 二叉树的最小深度

题目类型：二叉树、DFS、BFS

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个二叉树，找出其最小深度。最小深度是从根节点到最近叶子节点的最短
  路径上的节点数量。说明：叶子节点是指没有子节点的节点。
  
  解题方法：
  (1)递归
  需要递归到终点，不断返回当前最小深度。
  (2)非递归
  当我们找到一个叶子节点时，直接返回这个叶子节点的深度。广度优先搜索的性质
  保证了最先搜索到的叶子节点的深度一定最小。
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/er-cha-shu-de-zui-xiao-shen-du-by-leetcode-solutio/)）

  递归

  ```python
  class Solution:
      def minDepth(self, root: TreeNode) -> int:
  
          if root is None:
              return 0
          if root.left is None and root.right is None:
              return 1
  
          min_depth = 10 ** 9
          if root.left:
              min_depth = min(self.minDepth(root.left), min_depth)
          if root.right:
              min_depth = min(self.minDepth(root.right), min_depth)
  
          return 1 + min_depth
  ```

  非递归

  ```python
  import collections
  
  class Solution:
      def minDepth(self, root: TreeNode) -> int:
  
          if root is None:
              return 0
  
          deque = collections.deque([(root, 1)])
          while deque:
              node, depth = deque.popleft()
              # 第一个叶子结点
              if node.left is None and node.right is None:
                  return depth
              if node.left: deque.append((node.left, depth + 1))
              if node.right: deque.append((node.right, depth + 1))
  ```
  

## 长度最小的子数组

题目类型：数组

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个含有n个正整数的数组和一个正整数 target 。找出该数组中满足其和 ≥ target
  的长度最小的连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。
  如果不存在符合条件的子数组，返回 0 。
  
  解题方法：
  (1)暴力法
  时间复杂度：O(N*N)
  空间复杂度：O(1)
  
  (2)双指针法
  注意以下情况的返回值
  nums: [1, 1, 1, 1, 1, 1, 1, 1]
  target: 11
  实际ans值：8
  预计ans值：>= target
  不满足直接退出
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  暴力法

  ```python
  class Solution:
      # 暴力法
      def minSubArrayLen(self, target: int, nums: List[int]) -> int:
  
          if not nums:
              return 0
          ans = len(nums) + 1
          n = len(nums)
          for i in range(n):
              total = 0
              for j in range(i, n):
                  total += nums[j]
                  if total >= target:
                      ans = min(ans, j - i + 1)
          return ans
      # 双指针法
      def minSubArrayLen(self, target: int, nums: List[int]) -> int:
  ```

  双指针法

  ```python
  class Solution:
      def minSubArrayLen(self, target: int, nums: List[int]) -> int:
  
          if not nums:
              return 0
  
          left, right = 0, 0
          n = len(nums)
          ans = n + 1
          total = 0
  
          while right < n:
              total += nums[right]
              while total >= target:
                  ans = min(ans, right - left + 1)
                  total -= nums[left]
                  left += 1
              right += 1
  
          return 0 if ans == n + 1 else ans
  ```
