class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    """
    Time: O(n log n + m log m)
    Space: O(n + m)
    """