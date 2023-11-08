class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = []
        s = sorted(score)[::-1]
        for k in score:
            i = s.index(k)
            if i <= 2:
                if i == 0:
                    l.append("Gold Medal")
                elif i == 1:
                    l.append("Silver Medal")
                else:
                    l.append("Bronze Medal")
            else:
                l.append(str(i+1))
        return l