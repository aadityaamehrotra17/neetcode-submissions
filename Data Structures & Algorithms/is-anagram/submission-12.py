class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s, lst_t = [0]*26, [0]*26

        for i in s:
            pos = ord(i) - 97
            lst_s[pos] += 1
        
        for i in t:
            pos = ord(i) - 97
            lst_t[pos] += 1

        return lst_s == lst_t

    """
    Space: O(1)
    Time: O(n + m)
    """