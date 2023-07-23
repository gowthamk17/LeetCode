class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, "IV": 4, "V": 5, "IX":9, "X": 10, "XL":40, "L": 50, "XC": 90, "C": 100, "CD":400, "D": 500, "CM":900, "M": 1000}
        i = 0
        number = 0
        while(i < len(s)):
            if s[i] == "I" or s[i] == "X" or s[i] == "C":
                if s[i:i+2] in romans:
                    number += romans[s[i:i+2]]
                    i += 2
                    continue
            number += romans[s[i]]
            i += 1
        
        return number
            
            