class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteMap = {}
        magMap = {}
        for c in ransomNote:
            if c in noteMap:
                noteMap[c] += 1
            else:
                noteMap[c] = 1
        for c in magazine:
            if c in magMap:
                magMap[c] += 1
            else:
                magMap[c] = 1
        for k,v in noteMap.items():
            if k not in magMap or magMap[k] < v:
                return False
        return True
                