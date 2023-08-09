from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        max_len = max(map(len, wordDict))

        for i in range(1, n+1):
            for j in range(i-1, max(i-max_len-1, -1), -1):
                # only consider words that could fit
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == '__main__':
    s = 'leetcode'
    wordDict = ['leet', 'code']
    print(Solution().wordBreak(s, wordDict))

    s = 'applepenapple'
    wordDict = ['apple', 'pen']
    print(Solution().wordBreak(s, wordDict))

    s = 'catsandog'
    wordDict = ['cats', 'dog', 'sand', 'and', 'cat']
    print(Solution().wordBreak(s, wordDict))

    s = 'abcd'
    wordDict = ['a', 'abc', 'b', 'cd']
    print(Solution().wordBreak(s, wordDict))
