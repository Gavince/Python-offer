# 剑指Offer - 链表翻转及其变体题目总结

[toc]

## 反转链表I（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2:

- 问题描述

  ```python
  问题描述：
  输入一个链表，反转链表后，输出新链表的表头。
  
  解决方案：
  链表的遍历插入
  （1）迭代法
  时间复杂度：O(N)
  空间复杂度：O(1)
  （2）递归法
  ```

- 代码：迭代法（[解题思路](https://leetcode-cn.com/problems/reverse-linked-list/solution/shi-pin-jiang-jie-die-dai-he-di-gui-hen-hswxy/)）

  算法图解：

  <img src="./imgs/链表翻转.gif" style="zoom: 67%;" />

  ```python
  class Solution:
  
      def reverseList(self, pHead):
          """链表的翻转"""
  
          cur, pre = pHead, None
          while cur:
              tmp = cur.next
              cur.next = pre
              pre = cur
              cur = tmp
  
          return pre
  ```

- 代码：递归法（[解题思路](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/dong-hua-yan-shi-duo-chong-jie-fa-206-fan-zhuan-li/)）

  算法图解（**注意每次返回的都是同一个节点**）：

  ![](./imgs/11_递归.png)

  ```python
  class Solution:
      def reverseList(self, head: ListNode) -> ListNode:
  
          if head is None or head.next is None:
              return head
  
          node = self.reverseList(head.next)
          head.next.next = head
          head.next = None
  
          return node
  ```

## 反转链表II（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你单链表的头指针 head 和两个整数left和right ，其中left <= right。请你反转从位置 left到位
  置 right 的链表节点，返回 反转后的链表。
  
  示例：
  输入：head = [1,2,3,4,5], left = 2, right = 4
  输出：[1,4,3,2,5]
  
  解题方法：
  穿针引线
  时间复杂度：O(N)
  空间复杂度:O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/dong-hua-tu-jie-fan-zhuan-lian-biao-de-z-n4px/)）

  算法图解：

  ![](./imgs/111.png)

  ```python
  class Solution:
  
      def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
  
          # 申请哑节点
          dummmy = ListNode(0)
          dummmy.next = head
          # 记录
          count = 1
          pre = dummmy
          # 找到开头节点
          while pre.next and count < left:
              pre = pre.next
              count += 1
  
          cur = pre.next
          tail = cur
          # 局部翻转
          while cur and count <= right:
              nxt = cur.next
              # 节点插入连接
              cur.next = pre.next
              pre.next = cur
              # tail节点始终未变，只有指向在变换
              tail.next = nxt
              # 移动
              cur = nxt
              count += 1
  
          return dummmy.next
  ```

## K个一组翻转链表（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
  	给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。k 是
  一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那
  么请将最后剩余的节点保持原有顺序。
  进阶：
  你可以设计一个只使用常数额外空间的算法来解决此问题吗？
  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
  
  解题方法：
  仿照单链表的翻转
  1 2 3 4 5 6 k = 4
  4 3 2 1 
  ```

- 代码

  ```python
  class Solution:
      def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
  
          cur = head
          count = 0
          while cur and count < k:
              cur = cur.next
              count += 1
          if count == k:
              cur = self.reverseKGroup(cur, k)
              while count:
                  nxt = head.next
                  head.next = cur
                  cur = head
                  head = nxt
                  count -= 1
              head = cur
          return head
  ```

## 重排链表（<font color = red>重点</font>）

题目类型：链表

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个单链表 L 的头节点 head ，单链表 L 表示为：L0→ L1→ … → Ln-1→ Ln请
  将其重新排列后变为：L0→Ln→L1→Ln-1→L2→Ln-2→ …不能只是单纯的改变节点内部的值，而
  是需要实际的进行节点交换。
  
  解题方法：
  快慢指针 + 链表翻转 + 合并链表
  
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  快慢指针寻找中间节点（回文链表）

  ![](./imgs/97.png)

  ```python
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def reorderList(self, head: ListNode) -> None:
          """
          Do not return anything, modify head in-place instead.
          """
          # 快慢指针拆分
          slow, fast = head, head.next
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
          
          cur = slow.next
          slow.next = None
          # 逆转链表
          pre = None
          while cur:
              tmp = cur.next
              cur.next = pre
              pre = cur
              cur = tmp
          # 两个链表的合并
          l1, l2 = head, pre
          while l1 and l2:
              l1_tmp = l1.next
              l2_tmp = l2.next
  
              l1.next = l2
              l1 = l1_tmp
  
              l2.next = l1
              l2 = l2_tmp
  ```

## 回文链表（<font color = red>重点</font>）

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

  ![](./imgs/97.png)

- 链表翻转之后比较图解

  ![](./imgs/97-Page-2.png)

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

## 从尾到头打印链表

- 问题描述

  ```python
  问题描述：
  输入一个链表，按链表从尾到头的顺序返回一个ArrayList
  
  解决方案：
  递归（递归本身就是一种栈：先进后出）
  fun(node.next) + [node.val]
  [] + [8] + [7] + [5]
  [8, 7, 5]
  时间复杂度 O(N)： 遍历链表，递归 N 次。
  空间复杂度 O(N)： 系统递归需要使用 O(N) 的栈空间。
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/)）

  <img src="./imgs/tailtohead.png" style="zoom: 67%;" />

  ```python
  class Sulution:
  
      def reversePrint(self, head: ListNode) -> List[int]:
  
          if not head:
              return []
          
          return self.reversePrint(head.next) + [head.val]
  ```
