class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True
        if s == goal:
            return True
        # s_len = len(s)
        # for i in range(s_len):
        #     s = s[-1] + s[:-1]
        #     if s == goal:
        #         return True
        # return False
        s = s + s
        if s.find(goal) > -1:
            return True
        else:
            return False