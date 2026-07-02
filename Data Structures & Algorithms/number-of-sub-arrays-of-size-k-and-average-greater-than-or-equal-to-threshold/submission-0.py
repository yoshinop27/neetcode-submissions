class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = 0
        ret = 0
        for num in arr[:k]:
            window += num
        if window / k >= threshold:
            ret += 1
        for i in range(k, len(arr)):
            window -= arr[i-k]
            window += arr[i]
            if window/k >= threshold:
                ret += 1
        return ret

            

