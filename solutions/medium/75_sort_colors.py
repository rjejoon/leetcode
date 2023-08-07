from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        Dutch National Flag Problem
        '''
        i, j, k = 0, 0, len(nums) - 1
        # i keeps track of the 0
        # k keeps track of the 2
        # j is used to traverse the arr
        while j <= k:
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1

        print(nums)


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)

    nums = [1, 0, 2, 1]
    Solution().sortColors(nums)
