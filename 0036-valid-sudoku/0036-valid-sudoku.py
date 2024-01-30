class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    b = '(' + board[i][j] + ')'
                    row = str(i) + b
                    col = b + str(j)
                    cell = str(i // 3) + b + str(j // 3)
                    if row not in seen and col not in seen and cell not in seen:
                        seen.add(row)
                        seen.add(cell)
                        seen.add(col)
                    else:
                        return False
        return True