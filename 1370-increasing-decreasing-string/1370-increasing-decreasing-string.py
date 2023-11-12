class Solution:
    def sortString(self, s: str) -> str:
        ans = ""
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1  
        rev = False
        while count:
            if rev:
                for c in reversed(string.ascii_lowercase):
                    if c in count:
                        ans += c
                        count[c] -= 1
                        if count[c] == 0:
                            del count[c]
                rev = False
            else:
                for c in string.ascii_lowercase:
                    if c in count:
                        ans += c
                        count[c] -= 1
                        if count[c] == 0:
                            del count[c]
                rev = True
        return ans