class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for i in nums:
            if i in hash_set:  # O(1) BECAUSE IT'S A HASHSET
                return True

            hash_set.add(i)

        return False

"""
Space: O(n)
Time: O(n)
"""
