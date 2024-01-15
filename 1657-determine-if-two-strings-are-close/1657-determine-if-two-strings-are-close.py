class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0 for _ in range(26)]
        freq2 = [0 for _ in range(26)]
        for c in word1:
            freq1[ord(c) - ord('a')] += 1
        for c in word2:
            freq2[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if ((freq1[i] == 0) != (freq2[i] == 0)):
                return False
        
        freq1.sort()
        freq2.sort()
        
        for i in range(26):
            if (freq1[i] != freq2[i]):
                return False
        
        return True