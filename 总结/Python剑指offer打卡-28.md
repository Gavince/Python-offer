

# Python剑指offer打卡-28

[toc]

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

## 排序数组（<font color = red>重点</font>）

题目类型：排序

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  给你一个整数数组 nums，请你将该数组升序排列。
  
  解题思路：
  快速排序（比较点的选择增加随机性）和归并排序
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/)）

  快速排序

  ```python
  import random
  
  
  class Solution:
      def sortArray(self, nums: List[int]) -> List[int]:
  
          def quickSort(nums, strat, end):
              if strat >= end:
                  return 
              i, j = strat, end
              # 随机选择起始比较点
              index = random.randint(i, j)
              nums[i], nums[index] = nums[index], nums[i]
              pivot = nums[i]
              while i < j: 
                  while i < j and nums[j] >= pivot:
                      j -= 1
                  nums[i] = nums[j]
                  while i < j and nums[i] < pivot:
                      i += 1
                  nums[j] = nums[i]
              nums[i] = pivot
              quickSort(nums, strat, i - 1)
              quickSort(nums, i + 1, end)
          
          quickSort(nums, 0, len(nums) - 1)
          return nums
  ```

  归并排序

  ```python
  class Solution:
      def sortArray(self, nums: List[int]) -> List[int]:
  
          if len(nums) <= 1:
              return nums
  
          mid = len(nums) // 2
          left, right = nums[:mid], nums[mid:]
          # 拆分
          return self.merge(self.sortArray(left), self.sortArray(right))
  
      def merge(self, left, right):
  
          result = []
  
          # 公共部分比较合并
          while left and right:
              if left[0] < right[0]:
                  result.append(left.pop(0))
              else:
                  result.append(right.pop(0))
  
          # 剩余部分合并
          while left:
              result.append(left.pop(0))
          while right:
              result.append(right.pop(0))
  
          return result
  ```

## 数组中的逆序对（<font color = red>重点</font>）

题目类型：排序

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
  输入一个数组，求出这个数组中的逆序对的总数。
  
  示例：
  输入: [7,5,6,4]
  输出: 5
  
  解题方法：
  归并排序
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offer-51-shu-zu-zhong-de-ni-xu-pvn2h/)）

  ```python
  class Solution:
      def __init__(self):
          self.cnt = 0
  
      def reversePairs(self, nums: List[int]) -> int:
  
          self.mergeSort(nums)
          return self.cnt
  
      def mergeSort(self, nums):
  
          if len(nums) <= 1:
              return nums
  
          mid = len(nums) // 2
          left, right = nums[:mid], nums[mid:]
          # 拆分
  
          return self.merge(self.mergeSort(left), self.mergeSort(right))
  
      def merge(self, left, right):
  
          i, j = 0, 0
          result = []
          while i < len(left) and j < len(right):
  
              if left[i] <= right[j]:
                  result.append(left[i])
                  i += 1
              else:
                  result.append(right[j])
                  j += 1
                  self.cnt += (len(left) - i)
  
          result += left[i:]
          result += right[j:]
  
          return result
  ```


## 验证回文串

题目类型：回文串

题目难度：:star2:

- 问题描述

  ```
  问题描述：
      给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
  说明：本题中，我们将空字符串定义为有效的回文串。
  
  示例：
  输入: "A man, a plan, a canal: Panama"
  输出: true
  解释："amanaplanacanalpanama" 是回文串
  
  解题方法：
  （1）双指针
  时间复杂度：O(|s|)
  空间复杂度：O(|s|)
  （2）优化双指针
  时间复杂度：O(|s|)
  空间复杂度：O(|1|)
  ```

- 代码

  ```python
  class Solution:
      def isPalindrome(self, s: str) -> bool:
  
          # 构建回文串
          str_nums = "".join(ch.lower() for ch in s if ch.isalnum())
          left, right = 0, len(str_nums) - 1
          while left < right:
              if str_nums[left] != str_nums[right]:
                  return False
  
              left += 1
              right -= 1
  
          return True
  
      def isPalindrome(self, s: str) -> bool:
          # 构建回文串
          left, right = 0, len(s) - 1
          while left < right:
              # 寻找字符起点
              while left < right and not s[left].isalnum():
                  left += 1
              while left < right and not s[right].isalnum():
                  right -= 1
              if left < right:
                  # 需要不区分大小写
                  if s[left].lower() != s[right].lower():
                      return False
                  left += 1
                  right -= 1
  
          return True
  ```

## 验证回文字符串 II

题目类型：回文串

题目难度：:star2:

- 问题描述

  ```
  问题描述：
  给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
  
  示例:
  输入: s = "aba"
  输出: true
  
  解题方法：
  时间复杂度：O(|s|)
  空间复杂度：O(|1|)
  ```

- 代码

  ```python
  class Solution:
      def validPalindrome(self, s: str) -> bool:
  
          def checkpalindrome(low, high):
  
              while low < high:
                  if s[low] == s[high]:
                      low += 1
                      high -= 1
                  else:
                      return False
              return True
  
          left, right = 0, len(s) - 1
          while left < right:
              if s[left] == s[right]:
                  left += 1
                  right -= 1
              else:
                  # 删除一个字符，判断剩余字符串是否为回文字符串
                  return checkpalindrome(left + 1, right) or checkpalindrome(left, right - 1)
  
          return True
  ```

  