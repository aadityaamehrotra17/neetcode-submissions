class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        def count(n):
            res = 0
            while n:
                n &= n - 1
                res += 1
            return res
        arr = []
        for i in range(n+1):
            arr.append(count(i))
        return arr
        '''
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
