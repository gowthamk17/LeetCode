class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])
        answer = 0
        for c in range(k):
            for r in range(1, len(strs)):
                if strs[r][c] < strs[r-1][c]:
                    answer += 1
                    break
        return answer