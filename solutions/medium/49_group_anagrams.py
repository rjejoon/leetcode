from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_s_to_s = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            sorted_s_to_s[sorted_s].append(s)

        return list(sorted_s_to_s.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
