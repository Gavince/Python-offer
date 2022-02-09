# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 上午7:41
# @Author  : gavin
# @FileName: 26.判断是否是二叉搜索树的后序遍历序列结果.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/weixin_35154281

"""
问题描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,
否则输出No。假设输入的数组的任意两个数字都互不相同。

解决方案：

"""


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder:
            return True

        def isTree(postorder):
            """"递归循环测试"""

            root = postorder[-1]
            length = len(postorder)

            # 是否吗满足条件：左小有大对于根
            for i in range(length):
                if postorder[i] > root:
                    break

            # 右子树
            for j in range(i, length - 1):
                if postorder[j] < root:
                    return False
            left = True
            if i > 0:
                left = isTree(postorder[:i])
            right = True
            if i < length - 1:
                right = isTree(postorder[i:length - 1])
            return left and right

        return isTree(postorder)


if __name__ == "__main__":
    print(Solution().verifyPostorder([]))
