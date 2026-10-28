from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        most = 0
        left = 0
        res = 0
        for right, ch in enumerate(s):
            freqs[ch] += 1
            most = max(most, freqs[ch])
            while right - left + 1 - k > most:
                freqs[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        
        

         