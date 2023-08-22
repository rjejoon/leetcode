from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        dp = [0] * (max(nums) + 1)
        dp[1] = counts[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + i * counts[i])

        return dp[-1]


if __name__ == '__main__':
    nums = [3, 4, 2]
    print(Solution().deleteAndEarn(nums))

    nums = [2, 2, 3, 3, 3, 4]
    print(Solution().deleteAndEarn(nums))
