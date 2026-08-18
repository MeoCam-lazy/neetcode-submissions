class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Two strings are considered an anagram when a string is contains the exact same characters as the other string.
        # At beginning, my brain pop out an ideal that compare two set of the two strings but it got caught as testcase "xx" and "x". It is easy to understand because set of (xx) is exactly same as set of (x) because it eliminates duplicated characters. So i think the way to maintain whole string with out delete any character is to sort them and compare.
        s_s = sorted(s)
        s_t = sorted(t)
        return s_s == s_t
        