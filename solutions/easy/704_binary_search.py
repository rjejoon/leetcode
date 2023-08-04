from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    sol = Solution()
    print(sol.search(nums, target))

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    sol = Solution()
    print(sol.search(nums, target))

    nums = [5]
    target = 5
    sol = Solution()
    print(sol.search(nums, target))
