# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午10:31
# @Author  : gavin
# @FileName: 189.字母异位词分组.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
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
"""
import  collections


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


if __name__ == "__main__":
    obj = Solution()
    print(obj.groupAnagramsofCount(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
