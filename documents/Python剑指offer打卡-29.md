# Python剑指offer打卡-29

[toc]

## 最长回文串

题目类型：回文串

题目难度：:star2:

- 问题描述

  ```
  问题描述：
      给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
  在构造过程中，请注意区分大小写。比如"Aa"不能当做一个回文字符串。
  注意:假设字符串的长度不会超过 1010。
  
  解题方法：
  哈希表
  ```

- 代码  

  算法图解

  ![](./imgs/141.png)

  ```python
  class Solution:
      """不变动"""
      def longestPalindrome(self, s: str) -> int:
          # 中心扩展法
          def spread(l, r):
  
              count = 1
              while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                  l -= 1
                  r += 1
                  count += 2
  
              return count
  
          res = 0
          strs = list(s)
          # 奇数中心
          for i in range(len(strs)):
              res = max(res, spread(i, i))
          # 偶数中心
          for i in range(len(strs) - 1):
              res = max(res, spread(i, i + 1))
  
          return res
      
  import collections
  
  
  class Solution1:
      """重新构建"""
      def longestPalindrome(self, s: str) -> int:
  
          count = collections.Counter(s)
          ans = 0
  
          for v in count.values():
              # 偶数个数全添加
              ans += v // 2 * 2
              # 偶数中间添加奇数
              if ans % 2 == 0 and v % 2 == 1:
                  ans += 1
  
          return ans
  ```

## 二叉树的最大路径和

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

## 合并K个升序链表

题目类型：数组

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合
  并到一个升序链表中，返回合并后的链表。
  
  
  解题方法：
  构建最小堆，进行堆排序
  时间复杂度：O()
  空间复杂度：O()
  ```

- 解题方法

  ```python
  import heapq
  
  
  class Solution:
      def mergeKLists(self, lists: List[ListNode]) -> ListNode:
  
          if not List:
              return None
          if len(lists) == 1:
              return lists[0]
  
          dummy = cur = ListNode(-1)
          heap = []
          for node in lists:
              while node:
                  heapq.heappush(heap, node.val)
                  node = node.next
          # 构建有序链表
          while heap:
              cur.next = ListNode(heapq.heappop(heap))
              cur = cur.next
          return dummy.next
  ```

## 删除被覆盖的区间

题目类型：数组

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。只有当c <= a
  且b <= d时，我们才认为区间[a,b) 被区间[c,d) 覆盖。在完成所有删除
  操作后，请你返回列表中剩余区间的数目。
  
  解题方法：
  排序 + 遍历
  时间复杂度：O(NlogN)，其中N是区间的个数。
  空间复杂度：O(logN)，为排序需要的空间。
  ```

- 解题方法

  ```python
  class Solution:
      def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
  
          if not intervals:
              return 0
          # 先按照
          intervals.sort(key=lambda x: (x[0], -x[1]))
          ans, r_max = len(intervals), intervals[0][1]
          for i in range(1, len(intervals)):
              if intervals[i][1] <= r_max:
                  ans -= 1
              else:
                  r_max = max(r_max, intervals[i][1])
  
          return ans
  ```

## 缺失数字

题目类型：数组

题目难度：:star2:

- 问题描述

  ```
  问题描述：
      给定一个包含 [0, n]中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在
  数组中的那个数。
  进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
  解题方法：
  (1)位运算
  时间复杂度：O(N)
  空间复杂度：O(1)
  
  (2)求和公式
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 解题方法

  ```python
  class Solution:
      def missingNumber1(self, nums: List[int]) -> int:
  
          if not nums:
              return 0
  
          missing_num = len(nums)
          # 异或操作，保留最后的值
          for i, num in enumerate(nums):
              missing_num ^= (num ^ i)
  
          return missing_num
  
      def missingNumber2(self, nums: List[int]) -> int:
          if not nums:
              return 0
  
          exp_num = (len(nums) * (len(nums) + 1)) // 2
          act_num = sum(nums)
  
          return exp_num - act_num
  ```

  