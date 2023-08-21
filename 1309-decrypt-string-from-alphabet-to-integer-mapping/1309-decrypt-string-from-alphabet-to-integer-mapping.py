class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                answer += chr(int(s[i:i+2]) + 96)
                i += 3
                continue
            else:
                answer += chr(int(s[i]) + 96)
                i += 1
        return answer