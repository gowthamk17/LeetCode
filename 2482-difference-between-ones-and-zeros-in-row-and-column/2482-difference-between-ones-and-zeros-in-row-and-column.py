class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        diff = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            d = 0
            for j in range(col):
                if grid[i][j] == 1:
                    d += 1
                else:
                    d -= 1
            for j in range(col):
                diff[i][j] += d
        for j in range(col):
            d = 0
            for i in range(row):
                if grid[i][j] == 1:
                    d += 1
                else:
                    d -= 1
            for i in range(row):
                diff[i][j] += d
        return diff