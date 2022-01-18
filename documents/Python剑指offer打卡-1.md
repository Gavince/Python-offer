# 剑指offer打卡-1

[toc]

## 斐波那契数列

题目类型：数组、动态规划

题目难度：:star2:

- 问题描述

  ```python
  问题描述：
          写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐
  波那契数列的定义如下： 0 1 1 2 3 5 8 13　... F(n) = F(n-1) + F(n-2) (n > 2)斐波那契
  数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。答案需要取模
  1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
  
  解题方法：
  （1）递归
  有重复计算项, 时间复杂度O(2^n)
  
  （2）动态规划
  状态定义： 设 dp 为一维数组，其中dp[i] 的值代表斐波那契数列第 i 个数字 。
  转移方程： dp[i+1]=dp[i]+dp[i−1] ，即对应数列定义 f(n+1)=f(n)+f(n−1) ；
  初始状态： dp[0]=0, dp[1] = 1 ，即初始化前两个数字；
  返回值：     dp[n] ，即斐波那契数列的第 n 个数字。
          
  实际处理过程中，并不需要存储每一个dp状态的数值，因此：
  时间复杂度：O(N)
  空间复杂度：O(1)  使用双指针进行临时存储
  ```

  递归时间复杂计算：

  ![](./imgs/fi.png)

- 代码

  ```python
  class Solution:
  
      def fibonacci(self, n):
          """递归算法(时间复杂度极高O(n)=２^n)"""
          
          if n == 0:
              return 0
          if n == 1 or n == 2:
              return 1
          if n > 2:
              return self.fibonacci(n - 1) + self.fibonacci(n - 2)
  
      def fibonacci1(self, n):
          """动态规划问题"""
  	
      　a, b = 0, 1
          for _ in range(n):
              a, b = b, a+b
              
          return a%1000000007
  ```

## 跳台阶问题

题目类型：数组、动态规划

题目难度：:star2:

- 问题描述

  ```python
  问题描述1：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级
  的台阶总共有多少种跳法（先后次序不同算不同的结果）
  解决方案：
  当n=0 1（默认值）
  n=1 1 
  n=2 2
  n=3 3
  n=4 5
  ．．．．．．
  所以，符合斐波那契数列f(n) = f(n-1) + f(n-2)
  时间复杂度：O(n)
  空间复杂度：O(1)
  
  问题描述2：一只青蛙一次可以跳上1级台阶，也可以跳上2级,更可以一次跳上n级台阶
  求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
  解决方案：
  n = 0 0
  n = 1 1
  n = 2 2
  n = 3 4
  ．．．．．．
  所以，f(n) = 2f(n-1)
  
  时间复杂度：O(n)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/57xs06/)）

  ```python
  class Solution:
  
  # 问题一
      def numWays(self, n: int) -> int:
          a, b = 1, 1
          for _ in range(n):
              a, b = b, a + b
          
          return a%1000000007
      
  # 问题二
      def jump_floor(self, n: int):
   
          if n == 0 or n == 1 or  n == 2:
              return n
  
          return 2 * self.jump_floor(n - 1)
  ```

## 二维数据查找

题目类型：数组

题目难度：:star2:

- 问题描述与

  ```python
  问题描述：
  	在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增
  的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的
  一个二维数组和一个整数，判断数组中是否含有该整数,形式如下:
  1  2  3  4
  2  3  4  5
  6  7  8  9
  10 11 12 13
  解决方案：
  1.暴力搜索（遍历）
  时间复杂度：O(N^2)
  空间复杂度：O(1)
  
  2.考虑数据在存储位置上的存储性质
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
  
      def find(self, array, target):
          """不考虑时间复杂度，暴力搜索, T(O)=n^2"""
  
          for i in range(len(array)):
              for j in range(len(array[i])):
                  if array[i][j] == target:
                      return True
          return False
  
      def findNumberIn2DArray(self, matrix, target):
          """在二维数组中找到指定数字"""
  
          i, j = len(matrix)-1, 0
          while i >= 0 and j < len(matrix[0]):
              if matrix[i][j] > target: i -= 1
              elif matrix[i][j] < target: j += 1
              else: return True
  
          return False
  ```

## 使用两个栈实现一个队列

题目类型：栈和队列

题目难度：:star2:

- 问题描述

  ```python
  问题描述：
  用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
  
  解决方案：
  栈：先进后出(列表)
  队列：先进先出
  一个栈用来接收数据，另一个栈用来输出数据
  accept	output
          |4| ---- |1|
          |3| ---- |2|
          |2| ---- |3|
          |1| ---- |4|
  注意：只有当输出栈为空时，才能将接收栈内的数据传入
  ```
  
- 代码

  ```python
  class Solution:
  
      def __init__(self):
          self.accept_stack = []
          self.output_stack = []
  
      def push(self, val):
          self.accept_stack.append(val)
  
      def pop(self):
  
          if not self.output_stack:  # 输出栈空，返回值
              while self.accept_stack:
                  self.output_stack.append(self.accept_stack.pop())
  
          if self.output_stack:  # 有值
              return self.output_stack.pop()
          else:
              return None  # 输入、输出栈同时为空
  ```

## 替换空格

题目类型：字符串

题目难度：:star2:

- 问题描述

  ```python
  问题描述：
  	请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当
  字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
  
  解决方案：
  1. replace
  str = "hello world !"
  str.replace(" ", "%20")
  'hello%20world%20!'
  2.遍历元素
  自己仿写一个替换函数
  3.节省空间，按照实际需求进行替换
  ```

- 代码

  ```python
  class Solution:
  
      def replace_block(self, str):
  
          str = str.replace(" ", "%20")
  
          return str
  
      def replace_black1(self, str):
  
          new_str = []
  
          for i in range(len(str)):
              if str[i] == " ":
                  new_str.append("%20")
              else:
                  new_str.append(str[i])
          return ''.join(new_str)
  
      def replace_black2(self, str):
  
          if str is None:
              return None
  
          space_num = 0
          for i in range(len(str)):
              if str[i] == " ":
                  space_num += 1
  
          li = len(str) + 2 * space_num
          new_str = [1] * li
  
          p1 = len(str) - 1
          p2 = len(new_str) - 1
  
          while p1 >= 0:
              if str[p1] != " ":
                  new_str[p2] = str[p1]
                  p1 -= 1
                  p2 -= 1
              else:
                  new_str[p2] = "0"
                  new_str[p2 - 1] = "2"
                  new_str[p2 - 2] = "%"
                  p1 -= 1
                  p2 -= 3
  
          return "".join(new_str)
  ```

## 参考

[斐波那契数的时间复杂度、空间复杂度详解](https://blog.csdn.net/lxf_style/article/details/80458519)

[数据结构与算法题目](https://blog.csdn.net/storyfull/category_9475477_2.html)

[剑指offer（python）](https://blog.csdn.net/ggdhs/category_8914921.html)