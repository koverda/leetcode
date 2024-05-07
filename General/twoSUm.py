from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}  # remaining to target, index of original number

        for i in range(len(nums)):
            if nums[i] in rem:
                return [rem[nums[i]], i]
            rem[target - nums[i]] = i

sln = Solution()
res = sln.twoSum([2,7,11,15] , 9)
print(res)