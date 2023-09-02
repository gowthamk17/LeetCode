class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        result = []
        for word in words:
            eligible = True
            if word[0].lower() in first_row:
                for c in word:
                    if c.lower() not in first_row:
                        eligible = False
                        break
                if eligible:
                    result.append(word)
            elif word[0].lower() in second_row:
                for c in word:
                    if c.lower() not in second_row:
                        eligible = False
                        break
                if eligible:
                    result.append(word)
            else:
                for c in word:
                    if c.lower() not in third_row:
                        eligible = False
                        break
                if eligible:
                    result.append(word)
        return result
                