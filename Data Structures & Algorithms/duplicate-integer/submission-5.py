class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for i in nums:
            if i in seen:
                return True
            
            seen.append(i)

        return False

"""
hash_set = set()
for i in nums:
    if i in hash_set:
        return True
    hash_set.add(i)
return False

Space: O(n)
Time: O(n)
---------------------
num_set = set(nums)
return not (len(num_set) == len(nums))

Space: O(n)
Time: O(n)
"""
