class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_list = list(s)
        i = 0
        j = len(s_list) - 1
        while i < j:
            while i < j and not s_list[i].isalpha():
                i += 1
            while i < j and not s_list[j].isalpha():
                j -= 1
            if i < j:
                temp = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = temp
                i += 1
                j -=1
        return "".join(s_list)