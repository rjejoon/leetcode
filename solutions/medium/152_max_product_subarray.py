from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = 1
        res = float('-inf')
        for n in nums:
            vals = (n, curr_max * n, curr_min * n)
            curr_max = max(vals)
            curr_min = min(vals)
            res = max(res, curr_max)
        return res


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    print(Solution().maxProduct(nums))

    nums = [-2, 0, 1]
    print(Solution().maxProduct(nums))
