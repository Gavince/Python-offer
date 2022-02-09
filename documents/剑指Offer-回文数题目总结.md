# 剑指Offer-回文数题目总结

[toc]

## 回文数

题目类型：字符串

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述:
         给你一个整数x，如果x是一个回文整数，返回true；否则，返回
  false。回文数是指正序（从左向右）和倒序（从右向左）读都是一样
  的整数。例如，121 是回文，而 123 不是。
  进阶：你能不将整数转为字符串来解决这个问题吗？
  
  解题方法:
  (1)字符串判断
  s[::-1] == s
  
  (2)求整得头　＝＝　求余得尾
  情况１：当整数为负数时，不是回文数
  eg: -121(-121和121-不相等)
  
  情况２：当整数能够被10整除，且不为０时，不是回文数
  即不存在02020这种情况的整数
  eg: 120、112020
  
  情况3：数字长度奇偶情况下，退出原则
  while res < x:
  偶数：1221
  res: 1 12
  x:  122 12
  res == x
  奇数：121
  res: 1 12
  x: 12 1
  x = res // 10
  时间复杂度：O(N)
  空间复杂度:O(1)
  ```

- 代码

  图解代码思路

  ![](/home/gavin/Code/Python-offer/documents/imgs/106.png)

  ```python
  class Solution:
      def isPalindrome1(self, x: int) -> bool:
  
          s = str(x)
          return s == s[::-1]
  
      def isPalindrome2(self, x: int) -> bool:
  
          if x < 0 or (x % 10 == 0 and x != 0):
              return False
  
          res = 0
          while res < x:
              res = res * 10 + x % 10
              x = x // 10
  
          return x == res or x == res // 10
  ```

## 回文链表

题目类型：链表、回文数

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  请判断一个链表是否为回文链表。
  进阶：
  你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
  
  解题方法：
  （1）遍历（判断正向和反向结果是否一致）
  使用有个临时数组对遍历节点数值进行存储，并比较
  时间复杂度：O(n)  遍历所有节点
  空间复杂度：O(n)  临时数组
  （2）快慢指针
  两种情况：
   奇数：1 2 3 4 5  ||  4 3 2 1-->pre
   偶数：1 2 3 4  || 4 3 2 1-->pre
   用快慢指针寻找链表的中心位置，将链表进行分割l1和l2,并且已证明
  l1链表的长度始终大于等于l2链表的长度，因此将 l2 链表进行翻转与 l1
  链表进行比较。
  时间复杂度：O(n)  遍历所有节点
  空间复杂度：O(1) 没有使用额外空间
  
  注意：
  此题与链表翻转和排序链表知识点相同, 此外，只有一个节点时，链表是回文的。
  ```

- 图解快慢指针取中点

  ![](/home/gavin/Code/Python-offer/documents/imgs/97.png)

- 链表翻转之后比较图解

  ![](/home/gavin/Code/Python-offer/documents/imgs/97-Page-2.png)

- 代码（[解题思路](https://leetcode-cn.com/problems/palindrome-linked-list/solution/kuai-man-zhi-zhen-lian-biao-ni-xu-by-airesearcherj/)）

  ```python
  class Solution:
  
      def isPalindrom1(self, head):
          # 临时数组进行存储
          vars = []
          cur = head
          while cur:
              vars.append(cur.val)
              cur = cur.next
  
          return vars == vars[::-1]
  
      def isPalindrom2(self, head):
      
          if not head or not head.next:
              return True
          # 快慢指针
          slow, fast = head, head.next
          while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
          cur = slow.next
          slow.next = None
          pre = None
          # 链表翻转
          while cur:
              tmp = cur.next
              cur.next = pre
              pre = cur
              cur = tmp
          # 比较回文
          while pre:
              if head.val != pre.val:
                  return False
              head = head.next
              pre = pre.next
  
          return True
  ```

## 回文子串

题目类型：字符串

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
          给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被
  视作不同的子串。
  
  解题方法：
  （1）中心扩散法（注意偶数扩散和奇数扩散）
  方法在奇数下不能使用单个中心点得到偶数下的回文子串，因此，需要将
  偶数和奇数进行分别处理，高阶奇偶变化可以由低阶奇偶有限次扩展得到。
  时间复杂度:O(N^2)
  空间复杂度：O(1)
  
  （2）中心扩散法（消除奇偶，单层循环处理）
  枚举所有可能的中心点，有2*n - 1个中心点（共有n 个奇数中心点和n - 1个偶数中心点）
  时间复杂度:O(N^2)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/palindromic-substrings/solution/liang-dao-hui-wen-zi-chuan-de-jie-fa-xiang-jie-zho/)）

  图解中心位置

  ![](/home/gavin/Code/Python-offer/documents/imgs/101.png)

  ```python
  class Solution:
      def countSubstrings1(self, s: str) -> int:
  
          def spread(l, r):
              """中心扩散"""
              count = 0
              while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                  l -= 1
                  r += 1
                  count += 1
              return count
  
          res = 0
          # 奇数中心扩散
          for i in range(len(s)):
              res += spread(i, i)
          # 偶数中心扩散
          for i in range(len(s) - 1):
              res += spread(i, i + 1)
  
          return res
  
      def countSubstrings2(self, s: str) -> int:
          """暴力法"""
  
          n = len(s)
          ans = 0
  
          for i in range(2*n - 1):
              l, r = i//2, i//2 + i%2
              while l >= 0 and r < n and s[l] == s[r]:
                  l -= 1
                  r += 1
                  ans += 1
          return ans
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

  

