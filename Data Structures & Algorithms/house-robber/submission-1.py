class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        def parse(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            if i == n-1 or i == n-2:
                memo[i] = nums[i]
            else:
                memo[i] = nums[i] + max(parse(i+2), parse(i+3))
            return memo[i]
        return max(parse(0), parse(1))
        '''
        # Brute-Force
        n = len(nums)
        if n == 1:
            return nums[0]
        def parse(i):
            if i >= n:
                return 0
            elif i == n-1 or i == n-2:
                return nums[i]
            else:
                return nums[i] + max(parse(i+2), parse(i+3))
        return max(parse(0), parse(1))
        '''