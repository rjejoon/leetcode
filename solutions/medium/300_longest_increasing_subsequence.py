from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(nums))

    nums = [0, 1, 0, 3, 2, 3]
    print(Solution().lengthOfLIS(nums))

    nums = [7, 7, 7, 7, 7, 7, 7]
    print(Solution().lengthOfLIS(nums))

    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(Solution().lengthOfLIS(nums))
