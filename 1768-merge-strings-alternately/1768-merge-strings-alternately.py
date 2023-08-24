class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ''
        m = len(word1)
        n = len(word2)
        i,j = 0,0
        while i < m or j < n:
            if i < m:
                mergedString += word1[i]
                i += 1
            if j < n:
                mergedString += word2[j]
                j += 1
        return mergedString