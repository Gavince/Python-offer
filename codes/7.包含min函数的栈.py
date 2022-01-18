# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 下午7:42
# @Author  : gavin
# @FileName: 7.包含min函数的栈.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O(1))
解决方案：
1.构建一个和原栈相同的大小的保存最小值的序列
2.
list : 6 7 5 8 4
min  : 6   5   4
"""


# 版本一
class Stack:

    def __init__(self):

        self.stack = []
        self.min_value = []

    def pop(self):

        if self.stack is None:
            return None
        else:
            self.min_value.pop()
            return self.stack.pop()

    def push(self, val):

        self.stack.append(val)

        # 判断是否为最小值
        if self.min_value:
            if self.min_value[-1] < val:
                self.min_value.append(self.min_value[-1])
            else:
                self.min_value.append(val)
        else:
            self.min_value.append(val)

    def top(self):

        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def min(self):
        """返回栈中最小的元素"""
        if not self.stack:
            return None
        else:
            print(self.min_value)
            return self.min_value[-1]


#  版本二
class Stack1:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val):

        self.stack.append(val)

        if self.min_value:
            # 储存最小值
            if self.min_value[-1] >= val:
                self.min_value.append(val)
        else:
            # 初始值
            self.min_value.append(val)

    def pop(self):
        if not self.stack:
            return None
        else:
            # 保证有效数组的最小值
            if self.stack[-1] == self.min_value[-1]:
                self.min_value.pop()

            return self.stack.pop()

    def top(self):

        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def min(self):
        """抛出最小值，栈顶元素永远储存最小值"""

        if not self.stack:
            return None
        else:
            return self.min_value[-1]


if __name__ == "__main__":
    obj = Stack1()
    obj.push(6)
    obj.push(7)
    obj.push(5)
    obj.push(8)
    obj.push(4)
    obj.push(8)
    obj.push(4)
    obj.pop()


    print(obj.min())
