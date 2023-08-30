class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            freq = [0 for _ in range(26)]
            for c in s:
                freq[ord(c) - ord('a')] += 1
                if freq[ord(c) - ord('a')] == 2:
                    return True
        fi = -1
        si = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if fi == -1:
                    fi = i
                elif si == -1:
                    si = i
                else:
                    return False
        if si == -1:
            return False
        return s[fi] == goal[si] and s[si] == goal[fi]
                