from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1  # not enough flowers

        sortedDays = sorted(bloomDay)
        left = 0
        right = len(sortedDays) - 1
        mid = -1

        while left != right:
            mid = (left + right) // 2
            madeAll = self.madeAll(bloomDay, sortedDays[mid], k, m)

            # check if we're done
            if madeAll:
                right = mid
            else:
                left = mid + 1

        mid = (left + right) // 2
        return sortedDays[mid]

    def madeAll(self, bloomDay, day, k, m):
        toMake = m
        i = 0
        while i < len(bloomDay):
            if all(e <= day for e in bloomDay[i:i + k]) and i + k <= len(bloomDay):
                toMake -= 1
                i += k
            else:
                i += 1
        return toMake <= 0


sl = Solution()

# print(sl.minDays([1,2,4,9,3,4,1], 2, 2)) # 4
print(sl.minDays([1,10,3,10,2], 3, 1)) # 3