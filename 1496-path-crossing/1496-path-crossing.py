class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }
        visit = set((0,0))
        x,y = 0,0
        for c in path:
            visit.add((x,y))
            dx, dy = dir[c]
            x, y = dx+x, dy+y
            if (x,y) in visit:
                return True
        return False