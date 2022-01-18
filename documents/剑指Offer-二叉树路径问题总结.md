# 剑指Offer-二叉树路径问题总结

[toc]

## 二叉树中和为某一值的路径

题目类型：树

题目难度：:star2::star2::star2:

- 问题描述

  ```python
  问题描述：
          输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整
  数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形
  成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前).
  
  示例:
  给定如下二叉树，以及目标和 target = 22，
                [5]
                 / \
             [4]  [8]
             /       / \
          [11]  13[4]
            /  \      / \
          7  [2] [5] 1
  输出值：
  [
     [5,4,11,2],
     [5,8,4,5]
  ]
  
  解决方案：
  递归
  
  注意：
  路径表示为根结点到叶子结点的全路径
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/solution/mian-shi-ti-34-er-cha-shu-zhong-he-wei-mou-yi-zh-5/))

  图解算法

  ![](/home/gavin/Code/Python/剑指offer/总结/imgs/27.png)

  ```python
  class Solution:
  
      def FindPath(self, root, expectNumber):
  
          if root is None:
              return []
  
          res = []
          if root.val == expectNumber and root.left is None and root.right is None:
              res.append([root.val])
  
          left = self.FindPath(root.left, expectNumber - root.val)
          right = self.FindPath(root.right, expectNumber - root.val)
          for path in left + right:
              # 向上添加路径
              res.append([root.val] + path)
  
          return res
  ```

## 二叉树的最大路径和（<font color = red>重点</font>）

题目类型：二叉树

题目难度：:star2:

- 问题描述

  ```
  问题描述：
      路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点
  在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。路径和是路径中
  各节点值的总和。给你一个二叉树的根节点 root，返回其 最大路径和 。
  
  解题方法：
  DFS
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/)）

  ```python
  class Solution:
  
      def __init__(self):
          self.max_gain = float("-inf")
  
      def maxPathSum(self, root: TreeNode) -> int:
          def dfs(root):
              if root is None:
                  return 0
              # 计算左右结点收益
              left_gain = max(dfs(root.left), 0)
              right_gain = max(dfs(root.right), 0)
              # 更新当前结点的收益
              cur_gain = root.val + left_gain + right_gain
              self.max_gain = max(cur_gain, self.max_gain)
              # 只返回左右子树中的任意一个，保证路径的唯一性
              return root.val + max(left_gain, right_gain)
  
          dfs(root)
  
          return self.max_gain
  ```

  相似题目：二叉树的直径

## 二叉树的直径

题目类型：二叉树

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点
  路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
  
  实例：
  给定二叉树
  
            1
           / \
          2   3
         / \
        4   5
  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]
  
  解题方法：
  	题目相似与求解二叉树的深度，区别在于引入了直径的概念，深度的突破点在
  于左右分开，而直径则要求左右相连，且最大。
  深度优先遍历
  时间复杂度：O(N)
  空间复杂度：O(height)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/)）

  图解

  ![](./imgs/105.png)

  ```python
  class Solution:
      def diameterOfBinaryTree(self, root: TreeNode) -> int:
          self.ans = 0
  
          def dfs(root):
              if root is None: return 0
              left = dfs(root.left)
              right = dfs(root.right)
              cur_high = 1 + left + right
              self.ans = max(self.ans, cur_high)
  
              return max(left, right) + 1
  
          dfs(root)
  
          return self.ans - 1
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

## 
