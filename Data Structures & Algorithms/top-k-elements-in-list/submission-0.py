class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        frequency dictionary: store elements (keys) and their counts (values) in a dict
        bucket approach: now that we have the freq_dict, create an array of empty buckets
        bucket_array[i] = list of elements that appear i times
        access top k frequent elements from bucket and return the list
        '''
        freq = {}
        buck = [[] for i in range(len(nums)+1)]
        res = []

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        for kk, v in freq.items():
            buck[v].append(kk)

        for j in range(len(buck)-1, 0, -1):
            for z in buck[j]:
                res.append(z)
                if len(res) == k:
                    return res