class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            spaces = 0
            for c in sentence:
                if c == ' ':
                    spaces += 1
            spaces += 1
            if spaces > answer:
                answer = spaces
        return answer
            