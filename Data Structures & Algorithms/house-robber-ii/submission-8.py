class Solution:
    def rob(self, nums: List[int]) -> int:
        # new approach
        
        n = len(nums)

        if n <= 3:
            return max(nums)

        def parse(arr):
            l = len(arr)
            
            dp = [0] * l
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])

            for i in range(2,l):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])

            return dp[-1]

        return max(parse(nums[:n-1]), parse(nums[1:]))