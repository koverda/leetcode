class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = ""

        for i in range(len(s)):
            # make sure there's stuff to check
            if i + 1 < len(s):
                j = 0
                # check for even len palindrome
                right = i + 1 + j
                left = i - j
                while left >= 0 and right < len(s) and s[right] == s[left]:
                    print(left, right)
                    if right - left >= len(longest):
                        longest = s[left:right + 1]
                    j += 1
                    right = i + 1 + j
                    left = i - j

                j = 0
                right = i + j
                left = i - j
                # check for odd len palindrome
                while left >= 0 and right < len(s) and s[right] == s[left]:
                    if right - left >= len(longest):
                        longest = s[left:right + 1]
                    j += 1
                    right = i + j
                    left = i - j

        return longest