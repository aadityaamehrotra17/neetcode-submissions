class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        strs[i] contains only a - z
        using isAnagram requires sorting (nlogn complexity)
        create a dictionary that has specific count combinations as keys and a list of matching strs(anagrams) as values
        key of dict will be a tuple (list not allowed) of 26 elements indexed from 0 - 25 (a - z) with int vals representing char count
        return list of dict vals (.values() returns an object containing the list)
        defaultdict provides default value (in this case empty list) for non-existent keys
        '''
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        
        return list(res.values())
        # O(n*m) time
        # O(n) space