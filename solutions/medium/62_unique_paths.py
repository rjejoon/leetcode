class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(n):
                top = dp[i-1][j] if i-1 >= 0 else 0
                left = dp[i][j-1] if j-1 >= 0 else 0
                dp[i][j] = top + left

        return dp[-1][-1]


if __name__ == '__main__':
    m, n = 3, 7
    print(Solution().uniquePaths(m, n))

    m, n = 3, 2
    print(Solution().uniquePaths(m, n))
