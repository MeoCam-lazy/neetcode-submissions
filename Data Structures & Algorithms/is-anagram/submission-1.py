class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = sorted(s)
        set_t = sorted(t)
        return set_s == set_t
        