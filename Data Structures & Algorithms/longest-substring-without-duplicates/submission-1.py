class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ret = -float('inf')
        cur = set()
        for r in range(len(s)):
            if s[r] in cur:
                while s[r] in cur:
                    cur.remove(s[l])
                    l += 1
                cur.add(s[r])
            else:
                cur.add(s[r])
                ret = max(ret, len(cur))
        return 0 if ret == -float('inf') else ret

