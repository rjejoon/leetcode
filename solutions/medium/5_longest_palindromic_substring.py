class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_len = 0
        res = ''
        for i in range(len(s)):
            dp[i][i] = True
            max_len = 1
            res = s[i]

        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > max_len:
                        res = s[i:j+1]
                        max_len = j-i+1

        return res

    def longestPalindrome2(self, s: str) -> str:
        '''
        Expand around center
        Uses O(1) space
        No dp
        '''
        n = len(s)

        def expand_pallindrome(i, j):
            while 0 <= i <= j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return (i+1, j)

        res = (0, 0)
        for i in range(n):
            b1 = expand_pallindrome(i, i)
            b2 = expand_pallindrome(i, i+1)
            # find max based on the length of the pallindrome strings.
            res = max(res, b1, b2, key=lambda x: x[1]-x[0]+1)

        return s[res[0]:res[1]]


if __name__ == '__main__':
    s = 'aaaa'
    print(Solution().longestPalindrome(s))
