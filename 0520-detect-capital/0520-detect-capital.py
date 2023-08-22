class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            if len(word) == 1:
                return True 
            if word[1:].isupper():
                return True
            elif word[1:].islower():
                return True
            else:
                return False
        else:
            if word.islower():
                return True
            else:
                return False