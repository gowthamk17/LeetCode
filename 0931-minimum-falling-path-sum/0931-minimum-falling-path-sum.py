class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        
        for i in range(col):
            dp[0][i] = matrix[0][i]
            
        for i in range(1, row):
            for j in range(col):
                curr = matrix[i][j]
                left = right = float('inf')
                up = curr + dp[i-1][j]
                if j-1 >= 0:
                    left = curr + dp[i-1][j-1]
                if j+1 < col:
                    right = curr + dp[i-1][j+1]
                dp[i][j] = min(up, min(left, right))
        
        res = dp[row-1][0]
        for j in range(1, col):
            res = min(res, dp[row-1][j])
        
        return res
                    