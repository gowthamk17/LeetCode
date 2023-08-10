class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paraList = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        paraList = paraList.split()
        wordMap = {}
        for word in paraList:
            if word not in banned:
                if word in wordMap:
                    wordMap[word] += 1
                else:
                    wordMap[word] = 1
        return max(wordMap, key=wordMap.get)