class Solution:
    def hammingWeight(self, n: int) -> int:
        # use bin() to convert n to binary string and solve

        count = 0

        while n:
            # count += n % 2
            # n = n >> 1
            n &= n-1
            count += 1
        
        return count