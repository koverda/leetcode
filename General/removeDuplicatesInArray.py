from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return nums

        res = set()
        for n in nums:
            if n in res:
                continue
            res.add(n)

        nums = list(res)
        print(res)
        return len(res)

sln = Solution()
nums = [1,1,2,2,3,3]
res = sln.removeDuplicates(nums)
print(res, nums)

