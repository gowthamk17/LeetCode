class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = [0 for _ in range(26)]
        for c in s:
            charMap[ord(c) - ord('a')] += 1
        for c in t:
            charMap[ord(c) - ord('a')] -= 1
        for c in charMap:
            if c:
                return False
        return True