class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high_alt = 0
        cur_alt = 0
        for alt in gain:
            cur_alt += alt
            high_alt = max(high_alt, cur_alt)
        return high_alt