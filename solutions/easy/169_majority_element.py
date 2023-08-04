from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Based on Boyer-Moore Voting Algorithm
        Complexity: O(n) time, O(1) space
        '''
        n = len(nums)
        major = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:
                count += 1
                major = num
            elif major == num:
                count += 1
            else:
                count -= 1

        return major


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 2, 3, 4, 5]
    sol = Solution()
    expected = 1
    actual = sol.majorityElement(nums)
    print(actual)
    assert actual == expected
