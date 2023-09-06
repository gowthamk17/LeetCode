class Solution:
    def reverseWords(self, s: str) -> str:
            i = 0
            j = 0
            arr = []
            size = len(s)
            while i < size:
                while i < size and s[i] == ' ':
                    i += 1
                j = i
                while j < size and s[j] != ' ':
                    j += 1
                if i < size:
                    arr.append(s[i:j])
                i = j
            return ' '.join(arr[::-1])