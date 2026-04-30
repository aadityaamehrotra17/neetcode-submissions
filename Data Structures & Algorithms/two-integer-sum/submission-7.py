class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] in hash_map:
                return sorted([hash_map[nums[i]], i])

            hash_map[target - nums[i]] = i

        # for n in nums:
        #     if n in hash_map:
        #         return sorted([nums.index(n), nums.index(hash_map[n])])
            
        #     hash_map[target - n] = n            

    """
    Space: O(n)
    Time: O(n)
    """