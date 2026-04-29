class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        1. Use bin() to convert n to binary string and solve
        2. Check if lsb is 1 (%2), if yes increment count, shift right once, repeat till n is 0
        '''

        count = 0

        while n:
            count += n % 2
            n = n >> 1
            # n &= n-1
            # count += 1
        
        return count