class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_hash = {}
        res = -1
        
        for i in range(len(s)):
            if s[i] in char_hash:
                res = max(i-char_hash[s[i]]-1,res)
            else:
                char_hash[s[i]] = i
        
        return res