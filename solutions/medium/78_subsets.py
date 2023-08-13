from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(curr, i):
            if i >= len(nums):
                self.res.append(curr)
                return

            helper(curr, i+1)
            helper(curr + [nums[i]], i+1)

        helper([], 0)
        return self.res

    def subsets2(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    # assert solution.subsets(nums) == [[], [1], [2], [1, 2], [ 3], [1, 3], [2, 3], [1, 2, 3]]
    print(solution.subsets2(nums))
