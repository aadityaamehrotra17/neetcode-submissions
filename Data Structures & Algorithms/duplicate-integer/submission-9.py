class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for i in nums:
            if i in seen:  # THIS IS AN O(N) OPERATION, UNLIKE HASHSETS
                return True

            seen.append(i)

        return False

"""
Space: O(n)
Time: O(n2)
"""
