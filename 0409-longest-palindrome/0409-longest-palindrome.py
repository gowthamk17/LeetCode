class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpaired_chars = set()
        pairs = 0
        for char in s:
            if char in unpaired_chars:
                pairs += 2
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        return pairs+1 if unpaired_chars else pairs