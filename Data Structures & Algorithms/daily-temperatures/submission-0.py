class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        s = [] 
        for idx, num in enumerate(temperatures): 
            if s:
                while s and num > s[-1][1]:
                    pos, val = s.pop()
                    res[pos] = idx-pos
            s.append([idx,num])
        return res
        