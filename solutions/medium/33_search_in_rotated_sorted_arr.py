from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return mid
            
            if nums[lo] <= nums[mid]:
                # sorted
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # not sorted
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1 

        def helper(low, high):
            if low > high:
                return -1
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[high]:
                if target > nums[mid]:
                    return helper(low, mid-1)
                else:
                    return helper(mid+1, high)
            else:
                if target < nums[mid]:
                    return helper(low, mid-1)
                else:
                    return helper(mid+1, high)
        
        return helper(0, len(nums)-1)



if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    expected = 4
    actual = Solution().search(nums, target)
    print(f'expected: {expected}, actual: {actual}')

    target = 3
    expected = -1
    actual = Solution().search(nums, target)
    print(f'expected: {expected}, actual: {actual}')

    nums = [1]
    target = 0 
    expected = -1
    actual = Solution().search(nums, target)
    print(f'expected: {expected}, actual: {actual}')

    nums = [5,6,0,1,2,3,4]
    target = 6
    expected = 1
    actual = Solution().search(nums, target)
    print(f'expected: {expected}, actual: {actual}')
