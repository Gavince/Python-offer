# Python剑指offer打卡-33

[toc]

## 旋转链表

题目类型：双指针

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述:
      给你一个链表的头节点head，旋转链表，将链表每个节点向右移动k个位置。
  
  实例：
  输入：head = [1,2,3,4,5], k = 2
  输出：[4,5,1,2,3]
  
  解题方法：
  快满指针
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def rotateRight(self, head: ListNode, k: int) -> ListNode:
  
          if k == 0 or not head or not head.next:
              return head
          # 统计链表长度
          cur = head
          node_lens = 1
          while cur.next:
              cur = cur.next
              node_lens += 1
          k = k % node_lens
  
          # 快慢指针
          slow, fast = head, head
          for _ in range(k):
              fast = fast.next
          while fast.next:
              fast = fast.next
              slow = slow.next
          # 循环链接
          fast.next = head
          head = slow.next
          slow.next = None
  
          return head
  ```

## 两数相加II

题目类型：栈

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      给你两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储
  一位数字。将这两数相加会返回一个新的链表。你可以假设除了数字0之外，这两个数字都不会以零开
  头。
  
  实例:
  输入：l1 = [7,2,4,3], l2 = [5,6,4]
  输出：[7,8,0,7]
  
  解题方法：
  链表头插法
  时间复杂度：O(max(M, N))
  空间复杂度：O(M + N)
  ```

- 代码

  ```python
  class ListNode:
      def __init__(self, val=0, next=None):
          self.val = val
          self.next = next
  
  
  class Solution:
      def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  
          # 申请两个栈
          stack1 = []
          stack2 = []
          while l1:
              stack1.append(l1.val)
              l1 = l1.next
          while l2:
              stack2.append(l2.val)
              l2 = l2.next
  
          dummy = ListNode(0)
          carry = 0
          while stack1 or stack2 or carry:
              x = stack1.pop() if stack1 else 0
              y = stack2.pop() if stack2 else 0
              sum_ = x + y + carry
              carry = sum_ // 10
              # 头插法
              cur = ListNode(sum_ % 10)
              cur.next = dummy.next
              dummy.next = cur
  
          return dummy.next
  ```

## 字符串相加

题目类型：双指针

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      给定两个字符串形式的非负整数num1 和num2，计算它们的和并同样以字符串形式返回。
  你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符
  串转换为整数形式。
  
  解题方法：
  双指针
  时间复杂度：O(max(m, n))
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def addStrings(self, num1: str, num2: str) -> str:
          res = ""
          carry = 0
          i, j = len(num1) - 1, len(num2) - 1
          
          while i >= 0 or j >= 0:
              n1 = int(num1[i]) if i >= 0 else 0
              n2 = int(num2[j]) if j >= 0 else 0
              # 求解进位
              tmp = n1 + n2 + carry
              carry = tmp // 10
              res = str(tmp % 10) + res
              i -= 1
              j -= 1
  
          return "1" + res if carry else res
  ```

## 两数之和II

题目类型：双指针

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个已按照 非递减顺序排列的整数数组numbers ，请你从数组中找出两个数满足相加
  之和等于目标数target 。函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numb
  ers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <=
  numbers.length 。你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的
  元素。
  
  解题方法：
  注意有序性，使用哈希表的时间复杂度和空间复杂度分别为O(N)
  双指针
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def twoSum(self, numbers: List[int], target: int) -> List[int]:
  
          i, j = 0, len(numbers) - 1
  
          while i < j:
              sum_ = numbers[i] + numbers[j]
              if sum_ == target:
                  return [i + 1, j + 1]
              if sum_ < target:
                  i += 1
              else:
                  j -= 1
  
          return []
  ```

## 最长公共前缀

题目类型：纵向遍历

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共
  前缀，返回空字符串 ""。
  实例1:
  输入：strs = ["flower","flow","flight"]
  输出："fl"
  实例2：
  输入：strs = ["dog","racecar","car"]
  输出：""
  解释：输入不存在公共前缀。
  解题方法：
  纵向比较
  跳出原则:
  （1）比最小的数组长度还小
  （2）对应位置上的字符不相等
  时间复杂度：O(MN)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def longestCommonPrefix(self, strs: List[str]) -> str:
  
          if not strs:
              return ""
  
          length, count = len(strs[0]), len(strs)
          for i in range(length):
              c = strs[0][i]
              # 比较剩余部分
              if any(i == len(strs[j]) or c != strs[j][i] for j in range(1, count)):
                  return strs[0][:i]
  
          # 只有一个字符时
          return strs[0]
  ```
