class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = [] # 1,2 - 3,5
        new_start, new_end = newInterval # 6,7
        i = 0
        # place all windows that are before our new window 
        while i < len(intervals): # 0, 1, 2
            cur_start, cur_end = intervals[i] # 9,10
            if cur_end < new_start: # y,y
                result.append(intervals[i]) 
                i+=1 # 2
            else:
                break
        if i >= len(intervals):
            result.append(newInterval)
        # merge case
        while i < len(intervals): 
            cur_start, cur_end = intervals[i] # 9, 10
            if new_end >= cur_start: # n
                start = min(cur_start, new_start) 
                i += 1 
                end = max(cur_end, new_end) 
                while i < len(intervals) and intervals[i][0] <= new_end: 
                    end = max(end, intervals[i][1]) 
                    i += 1 
                result.append([start, end]) 
                break
            else:
                result.append(newInterval)
                break
        # left over windows
        for j in intervals[i:]: # 9, 10
            result.append(j)
        return result