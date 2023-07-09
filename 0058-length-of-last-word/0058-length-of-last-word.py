class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split(" ")
        for item in splitted[::-1]:
            if item != "":
                return int(len(item))
        