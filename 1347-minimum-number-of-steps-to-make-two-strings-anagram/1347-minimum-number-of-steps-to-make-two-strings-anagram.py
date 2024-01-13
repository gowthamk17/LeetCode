class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        res = 0
        for val in count.values():
            if val > 0:
                res += val
        return res