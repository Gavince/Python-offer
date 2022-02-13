# 剑指Offer-二叉树的深度专题

[toc]

##　二叉树的最大深度

题目类型：二叉树

题目难度：:star2:

- 问题描述

  ```
  问题描述：
          输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）
  形成树的一条路径，最长路径的长度为树的深度。
  
  实例：
  给定二叉树 [3,9,20,null,null,15,7]，
  深度: 3
  
  解法：
  (1)后续遍历DFS
  二叉树的深度=max(左子树的深度，右子树的深度) + 1
  
  (2)层序遍历(BFS)
  每一层的结点单独进行遍历，并设置计数
  
  知识点：
  树中的一个节点的深度是它到根节点的路径上的边的条数
  1> 一棵树只有一个节点或没有节点，它的深度是0；
  2> 二叉树的根节点只有左子树而没有右子树，那么可以判断，二叉树的深度应该是其左子树的深度加1；
  3> 二叉树的根节点只有右子树而没有左子树，那么可以判断，那么二叉树的深度应该是其右树的深度加1；
  4> 二叉树的根节点既有右子树又有左子树，那么可以判断，那么二叉树的深度应该是其左右子树的深度较大值加1。
  ```

- 代码

  DFS解法

  ```python
  class Solution:
  
      def maxDepth(self, root: TreeNode) -> int:
          """DFS"""
  
          if not root: return 0
  
          return max(self.maxDepth(root.left), self.maxDepth(root.right) )+ 1
  
  
          return res
  ```

  BFS解法

  ```python
  class Solution:    
      
      def maxDepth1(self, root: TreeNode) -> int:
          """层序遍历"""
  
          if not root: return None
          queue, res = [root], 0
          while queue:
              tmp = []
              # 每一层单独进行遍历
              for node in queue:
                  if node.left: tmp.append(node.left)
                  if node.right: tmp.append(node.right)
              queue = tmp
              res += 1
           return res
  ```

## 二叉树的最小深度

题目类型：二叉树

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

- 代码

  DFS解法

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

  BFS解法

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

## N叉树的最大深度

题目类型：树

题目难度：:star2::star2::star2:

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

  DFS解法

  ```python
  class Solution:
      def maxDepth(self, root: 'Node') -> int:
          if not root:
              return 0
          if not root.children:
              return 1
          
          return max(self.maxDepth(child) + 1 for child in root.children)
  ```

  BFS解法

  ```python
  class Solution:
      def maxDepth(self, root: 'Node') -> int:
  
          if root is None:
              return 0
          deque = [root]
          ans = 0
          while deque:
              deque = [child for node in deque for child in node.children]
              ans += 1
          return ans
  ```

## 