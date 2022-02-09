# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 下午8:18
# @Author  : gavin
# @FileName: 8.栈的压入、弹出序列 判断一个序列是否是该栈的弹出序列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281


"""
问题描述：
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等
。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的
弹出序列。（注意：这两个序列的长度是相等的）

解决方案：
我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

1 2 3 4 5
4 5 3 2 1(可行)
"""


def find_pop(push_value, pop_value):
    """
    :param push_value: 压栈序列
    :param pop_value: 弹出序列
    :return: 弹出序列是否可行
    """

    if not push_value and len(push_value) != len(pop_value):
        return None

    stack = []  # 使用一个栈来模拟栈的输出
    index = 0

    for item in push_value:
        stack.append(item)
        while stack and stack[-1] == pop_value[index]:
            stack.pop()
            index += 1

    return True if stack == [] else False


if __name__ == "__main__":
    li = [1, 2, 3, 4, 5]
    li1 = [4, 5, 3, 2, 1]
    li2 = [4, 5, 3, 1, 2]
    print(find_pop(li, li1))
    print(find_pop(li, li2))