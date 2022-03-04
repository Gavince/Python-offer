import sys


class Solution:
    pass


if __name__ == "__main__":
    # 1.单行数据输入,如: 3 2
    # m, n = map(int, sys.stdin.readline().split())
    # print(m, n)

    # 2.多行数据输入
    """
    3 2 （3个人，2次询问）
    1 5 6 （3个人苹果数目）
    1 （第一次寻问）
    3 （第二次询问）
    """
    m, n = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(int(input()))
    print(m, n, nums, ans)
