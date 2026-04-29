class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot, binary search both segments
        # edge case: len(nums) = 1 -> check if nums[0] is target
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        pivot = r #minimum element
        res = -1

        l, r = 0, pivot-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                res = m
                break
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        
        l, r = pivot, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                res = m
                break
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1

        return res        