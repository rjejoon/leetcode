from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        h_s, h_p = 0, 0
        res = []

        if n > m:
            return []

        for i in range(n):
            h_s += hash(s[i])
            h_p += hash(p[i])
        if h_s == h_p:
            res.append(0)

        for i in range(n, m):
            h_s += hash(s[i]) - hash(s[i-n])
            if h_s == h_p:
                res.append(i - n + 1)
        return res
