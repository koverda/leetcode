from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0

        for i in range(len(nums)):
            if nums[i] == val:
                j = i
                while j < len(nums)-1 and nums[j] == val:
                    j += 1
                if nums[j] != val:
                    nums[i] = nums[j]
                    nums[j] = val
                    i += 1
                if j == len(nums) - 1:
                    return i
            i += 1
            j += 1
        return i

s = Solution()
res = s.removeElement([4,5], 4)
print(res)