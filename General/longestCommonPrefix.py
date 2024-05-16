from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        if not strs or not strs[0]:
            return pre

        minLen = float('inf')

        for s in strs:
            minLen = min(minLen, len(s))

        for i in range(minLen):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return pre
            pre += char
            i += 1

        return pre

sln = Solution()
res = sln.longestCommonPrefix(["flower","flow","flight"])
print(res)