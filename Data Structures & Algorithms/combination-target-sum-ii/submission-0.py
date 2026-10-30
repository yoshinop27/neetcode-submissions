class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path, res = [], []
        candidates.sort()
        
        def dfs(i, rem): 
            # at target
            if rem == 0:
                res.append(path[:])
            # past length of array / no possible solutions left
            if i >= len(candidates) or candidates[i] > rem:
                return
            c = candidates[i]
            path.append(c)
            # try path with this candidate
            dfs(i+1, rem - candidates[i])
            # try path without this candidate
            path.pop()
            j = i + 1
            while j < len(candidates) and candidates[i]==candidates[j]:
                j+=1
            dfs(j, rem)

        dfs(0, target)
        return res
        
        
                

