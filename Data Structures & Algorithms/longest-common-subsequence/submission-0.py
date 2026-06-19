class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1) # width
        l2 = len(text2) # height
        memo = [[0]*(l1+1) for _ in range(l2+1)]
        for i in range(l1+1):
            memo[0][i] = 0
        for i in range(l2+1):
            memo[i][0] = 0  
        ## build up the table
        for i in range(1,l2+1): # height
            for j in range(1,l1+1): # width
                if text1[j-1] == text2[i-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j-1], memo[i][j-1], memo[i-1][j])
        return memo[l2][l1]