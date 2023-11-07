class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ans = ''
        pref = ''
        if str(num)[0] == '-':
            pref = '-'
            num = int(str(num)[1:])
        while num:
            ans = str(num % 7) + ans
            num //= 7
        if pref:
            ans = pref + ans
        return ans