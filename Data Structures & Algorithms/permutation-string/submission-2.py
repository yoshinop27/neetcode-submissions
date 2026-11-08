from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        comp = Counter([]) 
        l = 0
        for r,ch in enumerate(s2):
            # check
            if comp == counts:
                return True
            # add 
            comp[ch] += 1
            # maintain window size
            while r-l+1 > len(s1):
                l_ch = s2[l]
                comp[l_ch] -= 1
                l += 1
        if comp == counts:
            return True
        return False
            
            
            



