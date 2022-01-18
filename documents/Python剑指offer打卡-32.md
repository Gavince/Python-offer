# Python剑指offer打卡-32

[toc]

## 最长连续递增序列

题目类型：双指针

题目难度：:star2::star2:

- 问题描述

  ```
      给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
  连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，
  都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ...,
  nums[r - 1], nums[r]] 就是连续递增子序列。
  实例：
  1 2 5 8 6 3 4 5 6
  连续递增子序列】
  解题方法：
  双指针 + 滑动窗口
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def findLengthOfLCIS(self, nums: List[int]) -> int:
  
          if not nums: return 0
          ans = 0
          left = 0
          for right in range(len(nums)):
              if right > 0 and nums[right] <= nums[right - 1]:
                  left = right
              ans = max(ans, right - left + 1)
  
          return ans
  ```

## 和为S的两个数字

题目类型：双指针(对撞双指针)

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正
  好是s。如果有多对数字的和等于s，则输出任意一对即可。
  
  解题方法：
  双指针，对撞双指针
  时间复杂度：(N)
  空间复杂度:O(1)
  ```

- 代码

  ```python
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
  
          i, j = 0, len(nums) - 1
          while i < j:
              s = nums[i] + nums[j]
              if s > target:
                  j -= 1
              elif s < target:
                  i += 1
              else:
                  return [nums[i], nums[j]]
  
          return []
  ```

## 乘积最大数组

题目类型：双指针

题目难度：:star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字）
  ，并返回该子数组所对应的乘积。
  实例：
  nums = [2, 3, -2, 4]
  pre_max:2 pre_min:2
  cur_max: 6 cur_min: 3
  cur_max: -2 cur_min: -12
  cur_max: 4 cur_min: -48
  解题方法：
  时间复杂度：O(N)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def maxProduct(self, nums: List[int]) -> int:
  
          if not nums: return 0
          if len(nums) == 1: return nums[0]
          pre_min, pre_max = nums[0], nums[0]
          ans = nums[0]
  
          for i in range(1, len(nums)):
              cur_max = max(pre_min * nums[i], pre_max * nums[i], nums[i])
              cur_min = min(pre_min * nums[i], pre_max * nums[i], nums[i])
              ans = max(cur_max, ans)
              pre_max = cur_max
              pre_min = cur_min
  
          return ans
  ```

## 在排序数组中查找元素的第一个和最后一个位置

题目类型：二分法

题目难度：:star2::star2::star2::star2:

- 问题描述

  ```
  问题描述：
      给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
  如果数组中不存在目标值 target，返回[-1, -1]。
  
  解题方法：
  二分法
  时间复杂度：O(logN)
  空间复杂度：O(1)
  ```

- 代码

  ```python
  class Solution:
      def searchRange(self, nums: List[int], target: int) -> List[int]:
  
          if target not in nums: return [-1, -1]
  
          def helper(tar):
  
              l, r = 0, len(nums) - 1
              while l <= r:
                  mid = (l + r) // 2
                  if tar >= nums[mid]:
                      l = mid + 1
                  else:
                      r = mid - 1
              return l
  
          return [helper(target - 1), helper(target) - 1]
  ```

## 区间合并

题目类型：双指针

题目难度：:star2::star2:

- 问题描述

  ```
  问题描述：
      以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
  。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
  
  解题方法：
  排序合并
  ```

- 代码

  ```python
  from typing import List
  
  
  class Solution:
      def merge(self, intervals: List[List[int]]) -> List[List[int]]:
  
          intervals.sort(key=lambda x: x[0])
  
          merged = []
  
          for interval in intervals:
              # 判断区间的连续性
              if not merged or merged[-1][1] < interval[0]:
                  merged.append(interval)
              else:
                  # 合并
                  merged[-1][1] = max(merged[-1][1], interval[1])
  
          return merged
  ```

  