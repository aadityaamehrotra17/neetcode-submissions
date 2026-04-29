class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # look at hints

        if len(nums) < 2:
            return len(nums)
            
        store = set(nums)
        maxCount = 1
        
        for i in store:
            if i-1 in store:
                continue
            count = 1
            while True:
                if i+1 not in store:
                    break
                count += 1
                maxCount = max(count, maxCount)
                i += 1
        
        return maxCount