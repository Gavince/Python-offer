# Python剑指offer打卡-38

[toc]

## 有效三角形的个数

题目类型：贪心法

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形
  三条边的三元组个数。
  
  解题方法：
  原则：两边之和大于第三边
  
  方法一：二分法
  数组排序后满足：a <= b <= c
  一定存在：a + c > b，b + c > a
  需要证明：c < a + b
  二分法寻找可能的c值
  时间复杂度：O(n^2logn)
  空间复杂度：O(logn)
  
  方法二：双指针
  时间复杂度：O(n^2)
  空间复杂度：O(logn)
  ```

- 代码

  ```python
  class Solution:
      def triangleNumberofBinarySort(self, nums: List[int]) -> int:
  
          n = len(nums)
          nums.sort()
          ans = 0
          for i in range(n):
              for j in range(i + 1, n):
                  # 使用二分法查找第三个数字
                  left, right, k = j + 1, n - 1, j
                  # 在有序数组中寻找目标值
                  while left <= right:
                      mid = (left + right) // 2
                      if nums[mid] < nums[i] + nums[j]:
                          k = mid
                          left = mid + 1
                      else:
                          right = mid - 1
                  ans += k - j
  
          return ans
  
      def triangleNumberofDoublePoint(self, nums: List[int]) -> int:
  
          n = len(nums)
          nums.sort()
          ans = 0
          for i in range(n):
              k = i
              for j in range(i + 1, n):
                  # 遍历第三个结点c
                  # a, b, k + 1
                  # 1, 2, 3, 5, 7, 9
                  while k + 1 < n and nums[k + 1] < nums[j] + nums[i]:
                      k += 1
                  ans += max(k - j, 0)
  
          return ans
  ```

## 最小覆盖子串

题目类型：贪心法

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果
  s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
  注意：
  - 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
  - 如果 s 中存在这样的子串，我们保证它是唯一的答案。
  解题方法：
  滑动窗口
  ```

- 代码

  ```python
  class Solution:
  
      def minWindow(self, s: str, t: str) -> str:
          need = collections.defaultdict(int)
          # 初始化need字典
          for c in t:
              need[c] += 1
          # 统计还需要的数目
          needCnt = len(t)
          left = 0
          res = (0, float("inf"))
  
          # 滑动窗口
          for right, c in enumerate(s):
              # right
              if need[c] > 0:
                  needCnt -= 1
              need[c] -= 1
  
              # 滑动左窗口，并消除多余数目
              if needCnt == 0:
                  while True:
                      c = s[left]
                      # a, a
                      if need[c] == 0:
                          break
                      need[c] += 1
                      left += 1
                  if right - left < res[1] - res[0]:
                      res = (left, right)
                  # 寻找下一个位置
                  need[s[left]] += 1
                  needCnt += 1
                  left += 1
  
          return "" if res[1] > len(s) else s[res[0]: res[1] + 1]
  ```

## 字符串解码

题目类型：贪心法

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，
  表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数，你可以认为
  输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。此外，
  你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的
  输入。
  
  示例：
  输入：s = "3[a]2[bc]"
  输出："aaabcbc"
  
  解题方法：
  栈
  时间复杂度：O(N)
  空间复杂度：O(N)
  
  原题链接：https://leetcode-cn.com/problems/decode-string/
  ```

- 代码

  ```python
  class Solution:
      def decodeString(self, s: str) -> str:
  
          stack, res, multi = [], "", 0
          for c in s:
              if c == "[":
                  stack.append([res, multi])
                  # 重置
                  res, multi = "", 0
              elif c == "]":
                  last_res, cur_multi = stack.pop()
                  res = last_res + cur_multi*res
              elif "0" <= c <= "9":
                  # 进位运算， eg:121
                  multi = multi*10 + int(c)
              else:
                  res += c
          return res
  ```

## 有效的字母异位词

题目类型：贪心法

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
  注意：若s 和 t中每个字符出现的次数都相同，则称s和t互为字母异位词。
  
  示例：
  输入: s = "anagram", t = "nagaram"
  输出: true
  
  解题方法：
  字符匹配
  时间复杂度：O(s) s为匹配字符长度
  空间复杂度：O(S) S为总26长度
  ```

- 代码

  ```python
  class Solution:
      def isAnagram(self, s: str, t: str) -> bool:
  
          # 不相等，直接为False
          if len(s) != len(t):
              return False
          record = [0]*26
          # 记录标签值
          for i in range(len(s)):
              record[ord(s[i]) - ord("a")] += 1
              record[ord(t[i]) - ord("a")] -= 1
          # 判断是否满足条件
          for i in range(26):
              if record[i] != 0:
                  return False
  
          return True
  ```

## 分裂二叉树的最大乘积

题目类型：贪心法

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你一棵二叉树，它的根为root 。请你删除 1 条边，使二叉树分裂
  成两棵子树，且它们子树和的乘积尽可能大。由于答案可能会很大，请你将
  结果对 10^9 + 7 取模后再返回。
  
  解题方法：
  DFS
  时间复杂度：O(N)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree/
  ```

- 代码

  ```python
  class Solution:
      def maxProduct(self, root: TreeNode) -> int:
  
          # 记录各个结点的node_sum
          list_sum = []
  
          def dfs(root):
              if root is None: return 0
              cur_node_sum = dfs(root.left) + dfs(root.right) + root.val
              list_sum.append(cur_node_sum)
  
              return cur_node_sum
  
          total_sum = dfs(root)
          ans = float("-inf")
          for sum_ in list_sum:
              ans = max(ans, sum_ * (total_sum - sum_))
  
          return ans % (10 ** 9 + 7)
  ```
