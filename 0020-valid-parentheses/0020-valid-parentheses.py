class Solution:
    def isValid(self, s: str) -> bool:
        pdic = {"(": ")", "[":"]", "{":"}"}
        stack = list()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "["  or s[i] == "{":
                stack.append(s[i])
            elif stack and pdic[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True