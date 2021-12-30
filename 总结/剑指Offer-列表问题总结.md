# 剑指Offer-缺失数字问题总结

[toc]

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


## 数组中的重复数字

题目类型：数组

题目难度：:star2::star2::star2:

- 问题描述

  ```python
  问题描述：
  	在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中
  某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
  请找出数组中任意一个重复的数字。
  
  解题方法:
  方法一：
  集合
  时间复杂度：O(N)
  空间复杂度：O(N)
  
  方法二：
  重点理解数组元素值的限定问题
  原地交换：索引与值的对应关系（一对多），不重复情况下索引与值一一对应。
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/mian-shi-ti-03-shu-zu-zhong-zhong-fu-de-shu-zi-yua/)）

  原地交换图示（注意索引与值的对应关系）：

  

  ![](/home/gavin/Python/剑指offer/总结/imgs/41.图示.png)

  ```python
  class Solution:
  
      def findRepeatNumber(self, nums: [int]) -> int:
          """"集合"""
  
          dic = set()
          for num in nums:
              if num in dic: return num
              dic.add(num)
  
          return -1
  
      def findRepeatNumber_1(self, nums: [int]) -> int:
          """原地交换：索引与值的对应关系"""
          i = 0
          while i < len(nums):
              if nums[i] == i:  # 索引与值相对应
                  i += 1
                  continue
  
            if nums[nums[i]] == nums[i]: return nums[i]  # 索引与值(一对多)重复
              nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  #将值和索引交换到正确的索引位置上
  
          return -1
  ```

- 变形（需要打印出重复出现的数字）

- 问题描述

  ```
  	给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出
  现一次。找到所有出现两次的元素。
  你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
  实例：
  输入:
  [4,3,2,7,8,2,3,1]
  输出:
  [2,3]
  ```

- 代码

  ```python
  class Solution:
      def findDuplicates(self, nums: List[int]) -> List[int]:
  
          if not nums:
              return []
          
          res = []
          n = len(nums)
  
          for i in range(n):
              num = abs(nums[i])
              if nums[num - 1] < 0:
                  res.append(num)
              else:
                  nums[num - 1] = -nums[num - 1]
          
          return res
  ```

## 只出现一次的数字

题目类型：数组、位运算

题目难度：:star2:

- 问题描述

  ```
  问题描述：
  	给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出
  现两次。找出那个只出现了一次的元素
  
  解题思路：
  1. 交换律：a ^ b ^ c <=> a ^ c ^ b
  2. 任何数于0异或为任何数 0 ^ n => n
  3. 相同的数异或为0: n ^ n => 0
  
  实例：
  var a = [2,3,2,4,4]
  2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/single-number/comments/)）

  ```python
  class Solution:
      def singleNumber(self, nums) -> int:
          a = 0
          for num in nums:
              a = a ^ num
          return a
  ```

## 0~n-1中缺失的数字

题目类型：数组

题目难度：:star2::star2::star2:

==注意==：leetcode和牛客网题目条件中数组长度不一致，leetcode：[0, n-1], 牛客网：[0, n]

### leetcode

- 问题描述

  ```python
  问题描述：
  	一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个
  数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数
  字不在该数组中，请找出这个数字。
  
  解题方法：
  排序数组中的搜索问题，首先想到 二分法
  step 1：
  i = 0  j = 3  m = 1
  index 0 1 2 3
  array  0 1  3 4
  
  step 2：
  num[m] = m, i = m + 1 
  i = 2  j = 3  m = 2
  index 0 1 2 3
  array  0 1 | 3 4
  
  step 3：
  num[m] != m, j = m  - 1
  i = 2  j = 2  m = 2
  index 0 1 2 3
  array  0 1 | 3 | 4
  
  step 4：
  num[m] != m, j = m  - 1
  且 j > i 跳出，return i
  i = 2  j = 1  m = 2
  index 0 1 2 3
  array  0 1 | 3 | 4
  
  时间复杂度：O(logN)
  空间复杂度：O(1)
  ```

- 代码（[解题思路](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/solution/mian-shi-ti-53-ii-0n-1zhong-que-shi-de-shu-zi-er-f/)）

  ```python
  class Solution:
      def missingNumber(self, nums: List[int]) -> int:
          """二分法"""
  
          i, j = 0, len(nums) - 1
          while i <= j:
              m = (i + j) // 2
              if nums[m] == m:
                  i = m + 1
              else:
                  j = m - 1
  
          return i
  ```

### 牛客网（缺失数字）

- 问题描述

  ```python
  问题描述：
  从0,1,2,...,n这n+1个数中选择n个数，找出这n个数中缺失的那个数，要求O(n)尽可能小。
  
  实例：
  n = 9
  输入：[0,1,2,3,4,5,6,7,8]
  输出：9
  
  step 1：
  i = 0  j = 3  m = 1
  index 0 1 2 3
  array  0 1  2 3
  
  step 2：
  num[m] = m, i = m + 1 
  i = 2  j = 3  m = 2
  index 0 1 2 3
  array  0 1 | 2 3
  
  step 2：
  num[m] = m, i = m + 1 
  i = 3  j = 3  m = 3
  index 0 1 2 3
  array  0 1 | 2 | 3
  
  step 4：
  num[m] = m, i = m + 1 
  i =  4  j = 3  m = 3
  且 j > i 跳出，return i
  index 0 1 2 3
  array  0 1 | 2 | 3
  
  二分法时间复杂度为:O(logn)<O(n)
  ```

- 代码

  ```python
  class Solution:
      def solve(self , a ):
          # write code here
          i, j = 0, len(a) - 1
          while i <= j:
              m = (i + j) // 2
              if a[m] == m: i = m + 1
              else: j = m - 1
          return i
  ```
