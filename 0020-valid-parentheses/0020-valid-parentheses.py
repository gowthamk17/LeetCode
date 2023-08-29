class Solution:
    def isValid(self, s: str) -> bool:
        braceMap = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in braceMap:
                stack.append(c)
            elif stack and c == braceMap[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0