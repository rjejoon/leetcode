from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def gen_permute(i):
            if i == len(nums):
                res.append(nums[:])
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                gen_permute(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        gen_permute(0)
        return res
