class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        n = len(nums)
        total = (n*(n+1))//2
        return total - sum(nums)
        '''
        # X ^ X = 0, X ^ 0 = X, XOR is associative
        n = len(nums)
        res = 0
        # 0^1^2^3^...^n
        for i in range(n + 1):
            res ^= i
        # 0^0^1^1^2^2^....^n^n
        for i in nums:
            res ^= i
        # res = missing number
        return res