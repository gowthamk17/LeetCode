class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(left, right, s):
            if len(s) == n*2:
                res.append(s)
                return
            if left < n:
                solve(left+1, right, s+'(')
            if right < left:
                solve(left, right+1, s+')')
        solve(0, 0, "")
        return res
        