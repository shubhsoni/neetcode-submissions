class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = sorted(s)
        set2 = sorted(t)
        if (set1 == set2) and (len(s) == len(t)):
            return True
        return False