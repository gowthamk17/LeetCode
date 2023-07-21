class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(int(length/2)):
            temp = s[i]
            s[i] = s[length - i - 1]
            s[length - i - 1] = temp
            
        