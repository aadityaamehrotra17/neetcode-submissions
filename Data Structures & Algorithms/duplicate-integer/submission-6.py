class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O(nlogn)

        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                return True

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
---------------------
seen = []
for i in nums:
    if i in seen:  # THIS IS AN O(N) OPERATION, UNLIKE HASHSETS
        return True
    seen.append(i)
return False

Space: O(n)
Time: O(n2)
"""
