from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        0-1 knapsack problem
        '''
        sum_nums = sum(nums)
        target = sum_nums // 2
        dp = [True] + [False] * target
        dp[0] = True
        if sum_nums % 2 != 0:
            return False
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]

    def canPartition2(self, nums: List[int]) -> bool:
        '''
        Uses set for dp
        '''
        dp, sum_nums = set([0]), sum(nums)
        if sum_nums % 2 != 0:
            return False
        for num in nums:
            dp |= {num + x for x in dp}
        return sum_nums // 2 in dp
