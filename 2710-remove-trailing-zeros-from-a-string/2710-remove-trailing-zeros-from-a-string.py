class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # num = num[::-1]
        # answer = ''
        # for i in range(len(num)):
        #     if num[i] == '0':
        #         continue
        #     else:
        #         answer = num[i:]
        #         break;
        # return answer[::-1]
        i = len(num) - 1
        while i > 0:
            if num[i] == '0':
                i -= 1
                continue
            else:
                break;
        return num[:i+1]
            