class Solution:

    def generateParenthsis(self, n):

        res = []

        def dfs(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:
                res.append(paths)
                return

            dfs(paths + "(", left + 1, right)
            dfs(paths + ")", left, right + 1)

        dfs("", 0, 0)
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.generateParenthsis(2))
