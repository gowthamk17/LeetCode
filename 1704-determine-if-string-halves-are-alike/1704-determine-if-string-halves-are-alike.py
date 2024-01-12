class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) / 2
        vowel = "aeiouAEIOU"
        count = 0
        for i in range(len(s)):
            if i < mid:
                if s[i] in vowel:
                    count += 1
            else:
                if s[i] in vowel:
                    count -= 1
        return (count == 0)