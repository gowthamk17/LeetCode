class Solution:
    def toLowerCase(self, s: str) -> str:
        lowercase = ''
        for c in s:
            if ord(c) <= 90 and ord(c) >= 65:
                lowercase += chr(ord(c) + 32)
            else:
                lowercase += c
        return lowercase