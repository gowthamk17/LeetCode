class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loserMap = defaultdict(int)
        player = set()
        for match in matches:
            player.add(match[0])
            player.add(match[1])
            loserMap[match[1]] += 1
        
        only_winners = []
        for p in player:
            if p not in loserMap:
                only_winners.append(p)
        one_loss = []
        for loser in loserMap:
            if loserMap[loser] == 1:
                one_loss.append(loser)
        return [sorted(only_winners), sorted(one_loss)]