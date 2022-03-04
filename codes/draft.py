# class Solution:
#
#     def findFriendPos(self, height, n):
#
#         pos = [0]*n
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if height[j] > height[i]:
#                    pos[i] = j
#                    break
#         return pos
#
#
# if __name__ == "__main__":
#     N = int(input())
#     height = list(map(int, input().split()))
#     obj = Solution()
#     ans = obj.findFriendPos(height, N)
#     for i, val in enumerate(ans):
#         if i == len(ans) - 1:
#             print(val)
#         else:
#             print(val, end=" ")
# class Solution:
#
#     def findRighPosition(self, arr):
#
#         nums = sum(arr)
#         n = len(arr)
#         res = [0] * n
#         index, count = 1, 0
#         while count < nums:
#             if index % 10 == 0 or index % 7 == 0:
#                 i = (index%n) - 1
#                 res[i] += 1
#                 count += 1
#             index += 1
#
#         return res
#
#
# if __name__ == "__main__":
#     obj = Solution()
#     arr = list(map(int, input().split()))
#     ans = obj.findRighPosition(arr)
#     for i, val in enumerate(ans):
#         if i == len(ans) - 1:
#             print(val)
#         else:
#             print(val, end=" ")

class Solution:

    def findmindefend(self, arr):
        n = len(arr)
        # 聚合球队总战斗力
        sum_ = sum(arr)
        # 定义转态
        dp = []
        # 初始化
        for i in range(n + 1):
            tmp = []
            for j in range((sum_ // 2) + 1):
                tmp.append(0)
            dp.append(tmp)
        # 转态转移
        for i in range(1, n + 1):
            for j in range(1, (sum_ // 2) + 1):
                if j >= arr[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1]] + arr[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return sum_ - 2 * dp[n][(sum_ // 2)]


if __name__ == "__main__":
    obj = Solution()
    arr = list(map(int, input().split()))
    print(obj.findmindefend(arr))
