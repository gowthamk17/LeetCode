class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        re = ""
        hexdeci = "0123456789abcdef"
        while num > 0:
            rem = num % 16
            num //= 16
            re += hexdeci[rem]
        return re[::-1]
            