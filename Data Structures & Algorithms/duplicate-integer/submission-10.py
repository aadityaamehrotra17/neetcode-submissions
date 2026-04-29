class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O(nlogn)

        for index in range(1, len(nums)):  # O(n)
            if nums[index] == nums[index - 1]:
                return True

        return False

"""
Space: O(1)
Time: O(nlogn)
"""
