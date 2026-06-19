from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = defaultdict(list)
        for s in strs:
                arr = [0] * 26
                for c in s:
                    i = ord(c) - 97
                    arr[i] += 1
                key[tuple(arr)].append(s)
        ret = []
        for k,v in key.items():
            ret.append(v)
        return ret