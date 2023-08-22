import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)

        for i in range(1, n+1):
            if math.sqrt(i) == int(math.sqrt(i)):
                dp[i] = 1
                continue

            for j in range(1, math.ceil(i**(1/2))):
                dp[i] = min(dp[i], dp[i-j**2] + 1)

        return dp[n]


if __name__ == '__main__':
    n = 12
    print(Solution().numSquares(n))

    n = 13
    print(Solution().numSquares(n))

    n = 8
    print(Solution().numSquares(n))
