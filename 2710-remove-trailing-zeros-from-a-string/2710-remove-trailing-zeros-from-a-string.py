class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        answer = ''
        for i in range(len(num)):
            if num[i] == '0':
                continue
            else:
                answer = num[i:]
                break;
        return answer[::-1]