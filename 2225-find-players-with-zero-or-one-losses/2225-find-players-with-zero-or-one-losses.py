class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loserMap = defaultdict(int)
        for winner, loser in matches:
            if loserMap[winner] == 0:
                loserMap[winner] = -1
            if loserMap[loser] == -1:
                loserMap[loser] = 1
            else:
                loserMap[loser] += 1
        only_winners = []
        one_loss = []
        for loser in loserMap:
            if loserMap[loser] == -1:
                only_winners.append(loser)
            if loserMap[loser] == 1:
                one_loss.append(loser)
        return [sorted(only_winners), sorted(one_loss)]