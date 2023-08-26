class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        good_stack = [s[0]]
        for i in range(1, len(s)):
            c = s[i]
            if c.islower():
                if len(good_stack) > 0 and c.upper() == good_stack[-1]:
                    good_stack.pop()
                else:
                    good_stack.append(c)
            else:
                if len(good_stack) > 0 and c.lower() == good_stack[-1]:
                    good_stack.pop()
                else:
                    good_stack.append(c)
        return ''.join(good_stack)