class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #edge case: len(heights) = 2 -> return min(heights)
        maxCapacity = min(heights)
        i, j = 0, len(heights)-1

        while i<j:
            capacity = (j-i) * min(heights[i],heights[j])
            maxCapacity = max(capacity, maxCapacity)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return maxCapacity