# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 下午9:21
# @Author  : gavin
# @FileName: 4.替换空格.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

解决方案：
1. replace
str = "hello world !"
str.replace(" ", "%20")
'hello%20world%20!'
2.遍历元素
自己仿写一个替换函数
3.节省空间，按照实际需求进行替换
"""


class Solution:

    def replace_block(self, str):

        str = str.replace(" ", "%20")

        return str

    def replace_block1(self, str):

        new_str = []

        for i in range(len(str)):
            if str[i] == " ":
                new_str.append("%20")
            else:
                new_str.append(str[i])
        return ''.join(new_str)

    def replace_block2(self, str):

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


if __name__ == "__main__":
    obj = Solution()
    str1 = "Hello world   ! "
    print(obj.replace_block(str1))
    print(obj.replace_block1(str1))
    print(obj.replace_block2(str1))
