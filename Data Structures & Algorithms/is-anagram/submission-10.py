class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s, set_t = {}, {}

        for i in s:
            set_s[i] = set_s.get(i, 0) + 1
        
        for i in t:
            set_t[i] = set_t.get(i, 0) + 1

        return set_s == set_t

    """
    Space: O(n + m)
    Time: O(n + m)
    """