# 剑指Offer-二叉树遍历

[toc]

## 二叉树的中序遍历（<font color = red>重点</font>）

**三种题目**：前序遍历、后序遍历、中序遍历

**两种做法**：DFS与BFS

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

## 从上往下打印二叉树（<font color = red>重点</font>）

**三种题型**：层序遍历，每一层打印遍历，“之”字形遍历

题目类型：树

题目难度：:star2::star2::star2:

- 问题描述

  ```python
  问题描述：
  从上往下打印出二叉树的每个节点，同层节点从左至右打印
  
  解决方案：
  简单的层序遍历
  ```

- 代码

  层序遍历

  ```python
  class Solution:
      
          def levelOrder(self, root: TreeNode) -> List[int]:
              """"层序遍历"""
              
                  if not root: return []
                  
                  res, queue = [], collections.deque()
                  queue.append(root)
                  
                  while queue:
                          node = queue.popleft()
                          res.append(node.val)
                          if node.left: queue.append(node.left)
                          if node.right: queue.append(node.right)
                              
         	        return res
  ```

  每一层打印遍历

  ```python
  class Solution:	
      
         def levelOrder(self, root):
  		"""层序遍历（每一层遍历）"""
          
  		if root is None: return []
  		res, deque = [], collections.deque()
  		deque.append(root)
  		
  		while deque:
  			tmp = []
  			for _ in range(len(deque)):
  				node = deque.popleft()
  				tmp.append(node.val)
  				if node.left: deque.append(node.left)
  				if node.right: deque.append(node.right)
  			res.append(tmp)
  
  		rerurn res
  ```

  之”字形遍历

  ```python
  class Solution:
      
          def levelOrder(self, root: TreeNode) -> List[List[int]]:
              	"""Z字形遍历"""
                  
                  if not root: return []
                  res, deque = [], collections.deque([root])
  
                  while deque:
                      tmp = collections.deque()
                      for _ in range(len(deque)):
                          node = deque.popleft() # 从左向右遍历
                          if len(res) % 2: tmp.appendleft(node.val) # 奇数层,队列首部
                          else: tmp.append(node.val) # 偶数层，队列尾部
                          if node.left: deque.append(node.left)
                          if node.right: deque.append(node.right)
  
                      res.append(list(tmp))
                      
                  return res
  ```

## 二叉树的右视图（<font color = red>重点</font>）

题目类型：二叉树

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
  
  解题方法：
  层序遍历
  ```

- 代码（[解题方法](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/)）

  ```python
  import collections
  
  
  class Solution:
      def rightSideView(self, root: TreeNode) -> List[int]:
  
          if root is None:
              return []
          res = []
          deque = collections.deque([root])
          while deque:
              tmp = []
              for _ in range(len(deque)):
                  node = deque.popleft()
                  tmp.append(node.val)
                  if node.left: deque.append(node.left)
                  if node.right: deque.append(node.right)
              res.append(tmp[-1])
          
          return res
  ```
