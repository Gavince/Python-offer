# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 上午9:51
# @Author  : gavin
# @FileName: 49.字符串的排列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281
"""
问题描述：
    输入一个字符串，打印出该字符串中字符的所有排列。你可以以任意顺序返回这个字符
串数组，但里面不能有重复元素。

实例：
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

解题方法：
回朔法
注意放回数组里面不能包含有重复元素，需要对其进行去重

原题链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
"""


class Solution:

    def permutation(self, s: str) -> List[str]:

        c, res = list(s), []

        def dfs(x):

            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换

        dfs(0)
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.permutation("abc"))
    # 验证是否去除重复元素
    print(obj.permutation("aab"))
