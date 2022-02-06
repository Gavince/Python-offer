# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 上午7:39
# @Author  : gavin
# @FileName: 139.验证回文串.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略
字母的大小写。
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

原题链接：https://leetcode-cn.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome1(self, s: str) -> bool:

        # 构建回文串
        str_nums = "".join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(str_nums) - 1
        while left < right:
            if str_nums[left] != str_nums[right]:
                return False

            left += 1
            right -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
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
