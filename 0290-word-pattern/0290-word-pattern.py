class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap = {}
        stringList = s.split(' ')
        for c in pattern:
            if stringList:
                string = stringList.pop(0)
            else:
                return False
            if c not in patternMap:
                if string in patternMap.values():
                    return False
                else:
                    patternMap[c] = string
            else:
                if patternMap[c] != string:
                    return False
        if stringList:
            return False
        else:
            return True