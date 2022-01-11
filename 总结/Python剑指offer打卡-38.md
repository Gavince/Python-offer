# Python剑指offer打卡-38

[toc]

## 划分字母区间

题目类型：贪心法

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      字符串 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母
  最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
  
  解题方法：
  贪心法
  时间复杂度：O(N)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/partition-labels/solution/
  ```

- 代码

  ```python
  class Solution:
      def partitionLabels(self, s: str) -> List[int]:
  
          # 统计每一个字符的最大右边界
          hast_table = [0] * 26
          for i, c in enumerate(s):
              hast_table[ord(c) - ord("a")] = i
          # 划分区间
          # 寻找最优边界
          res = []
          left, right = 0, 0
          for i, c in enumerate(s):
              # 扩充边界
              # 在当前区间内是否含有比当前值所在边界大的索引边界
              right = max(right, hast_table[ord(c) - ord("a")])
              if i == right:
                  res.append(right - left + 1)
                  left = right + 1
  
          return res
  ```

## 腐蚀的橘子

题目类型：BFS

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
  在给定的网格中，每个单元格可以有以下三个值之一：
  值0代表空单元格；
  值1代表新鲜橘子；
  值2代表腐烂的橘子。
  每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
  返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回-1。
  
  解题方法：
  BFS
  时间复杂度：O(mn)
  空间复杂度：O(mn)
  
  原题链接：https://leetcode-cn.com/problems/rotting-oranges/
  ```

- 代码

  ```python
  class Solution:
      def orangesRotting(self, grid) -> int:
  
          m, n = len(grid), len(grid[0])
          # 标记腐烂橘子的位置
          time = 0
          deque = []
          for i in range(m):
              for j in range(n):
                  if grid[i][j] == 2:
                      deque.append((i, j, time))
  
          # 开始腐烂新鲜橘子
          while deque:
              i, j, time = deque.pop(0)
              for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                  if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                      grid[i + di][j + dj] = 2
                      deque.append((i + di, j + dj, time + 1))
          # 无法腐蚀的橘子
          for row in grid:
              if 1 in row: return -1
  
          return time
  ```

## 整数拆分

题目类型：数学

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的
  乘积最大化。 返回你可以获得的最大乘积。
  
  
  解题方法：
  数学推导
  时间复杂度：O(1)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/integer-break/
  ```

- 代码

  ```python
  class Solution:
      def integerBreak(self, n: int) -> int:
  
          if n <= 3: return n - 1
          # 求解整数和余数
          a, b = n//3, n%3
          if b == 0: return 3**(a)
          if b == 1: return 3**(a - 1)*4
          return 3**(a)*2
  ```

## 字母异位词分组

题目类型：排序

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回
  结果列表。字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词
  中的字母通常恰好只用一次。
  
  解题方法：
  方法1:
  排序：由于互为字母异位词的两个字符串包含的字母相同，因此对两个字符串分别进
  行排序之后得到的字符串一定是相同的，故可以将排序之后的字符串作为哈希表的
  键。
  方法2:
  计数：相同字符下的字符编码相同
  时间复杂度：O(nklogk)
  空间复杂度：O(nk)
  
  原题链接：https://leetcode-cn.com/problems/group-anagrams/
  ```

- 代码

  ```python
  class Solution:
      def groupAnagramsofRank(self, strs):
          mp = collections.defaultdict(list)
  
          for str in strs:
              # 属于同一变换下的字符排序结果相同
              key = "".join(sorted(str))
              mp[key].append(str)
  
          return list(mp.values())
  
  
      def groupAnagramsofCount(self, strs):
          mp = collections.defaultdict(list)
  
          for str in strs:
              counts = [0]*26
              for c in str:
                  counts[ord(c) - ord("a")] += 1
  
              mp[tuple(counts)].append(str)
  
          return list(mp.values())
  ```

## 数字1的个数

题目类型：数学

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
  
  解题方法：
  数学推导
  时间复杂度：O(N)
  空间复杂度：O(1)
  
  原题链接：https://leetcode-cn.com/problems/number-of-digit-one/
  ```

- 代码

  图解算法

  ![](./imgs/190.png)

  ```python
  class Solution:
      def countDigitOne(self, n: int) -> int:
  
          dight, res = 1, 0
          cur, low, high = n % 10, 0, n // 10
          while high != 0 or cur != 0:
              if cur == 0:
                  res += high * dight
              elif cur == 1:
                  res += high * dight + 1 + low
              else:
                  res += high * dight + dight
              # 更新位置
              low += cur * dight
              cur = high % 10
              high = high // 10
              dight = dight * 10
  
          return res
  ```

## 