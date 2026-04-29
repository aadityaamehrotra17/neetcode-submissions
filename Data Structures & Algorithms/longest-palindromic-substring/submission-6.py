class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand from center
        if len(s) == 1:
            return s[0]

        store = {}
        large = 1

        for i in range(len(s)):
            # odd
            size, l, r = 1, i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                store[size] = s[l:r+1]
                size += 2
                l -= 1
                r += 1
            large = max(size-2, large)

            #even
            size, l, r = 0, i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                size += 2
                store[size] = s[l:r+1]
                l -= 1
                r += 1
            large = max(size, large)

        return store[large]