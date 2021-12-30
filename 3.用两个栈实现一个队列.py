# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 下午8:54
# @Author  : gavin
# @FileName: 3.用两个栈实现一个队列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

解决方案：
栈：先进后出(列表)
队列：先进先出

一个栈用来接收数据，另一个栈用来输出数据
"""


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
        else:  # 输出输出栈同时为空
            return None


if __name__ == "__main__":
    obj = Solution()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    # 1 2 3
    print(obj.pop())
    obj.push(555)
    print(obj.pop())
    print(obj.pop())
    obj.push(55)
    print(obj.pop())
    print(obj.pop())