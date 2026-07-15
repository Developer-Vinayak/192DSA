from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1count = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i:i+len(s1)]
            if Counter(window) == s1count:
                return True
        return False
