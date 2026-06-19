from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lets = defaultdict(int)
        for ch in s:
            s_lets[ch] += 1
        for ch in t:
            if not s_lets[ch]:
                return False
            s_lets[ch]-=1
        if all(v == 0 for v in s_lets.values()):
            return True
        return False