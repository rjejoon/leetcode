class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        res = 1
        for i in range(len(s)):
            dp[i][i] = 1

        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = dp[i+1][j-1] + 2
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return res


if __name__ == '__main__':
    s = "bbbab"
    print(Solution().longestPalindromeSubseq(s))

    s = "cbbd"
    print(Solution().longestPalindromeSubseq(s))
