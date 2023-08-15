class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if 0 < i and 0 < j:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
                else:
                    top = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = max(top, left)

        return dp[-1][-1]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    print(Solution().longestCommonSubsequence(text1, text2))

    text1 = "abc"
    text2 = "abc"
    print(Solution().longestCommonSubsequence(text1, text2))

    text1 = "abc"
    text2 = "def"
    print(Solution().longestCommonSubsequence(text1, text2))

    text1 = "bsbininm"
    text2 = "jmjkbkjkv"
    print(Solution().longestCommonSubsequence(text1, text2))
