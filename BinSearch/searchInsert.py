from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                break

        if nums[mid] >= target:
            return mid
        else:
            return mid + 1



sl = Solution()
print(sl.searchInsert([1,3,5,6], 7))