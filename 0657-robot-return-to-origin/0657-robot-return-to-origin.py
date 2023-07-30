class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coords = [0,0]
        for char in moves:
            if char == 'R':
                coords[0] += 1
            elif char == 'L':
                coords[0] -= 1
            elif char == 'U':
                coords[1] += 1
            elif char == 'D':
                coords[1] -= 1
        if coords[0] == 0 and coords[1] == 0:
            return True
        else:
            return False