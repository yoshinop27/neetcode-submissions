class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
             return len(arr)
        l = 0
        r=1
        prev = None
        ret = 1
        while r < len(arr):
            print(r)
            flag = arr[r-1] < arr[r]
            print(f'{r},{l}')
            print(flag)
            if flag != prev and arr[r-1] != arr[r]:
                ret = max(ret, r-l+1)
                prev = flag
                r+=1
            elif arr[r-1] == arr[r]:
                l = r
                r+=1
            else:
                l = r -1
                prev = None
        return ret