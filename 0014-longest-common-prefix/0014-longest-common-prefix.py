class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = strs[0]
        result = 0
        
        for i in range(len(sample)):
            isBreak = False
            for string in strs:
                if (i > len(string) - 1) or not (string[i] == sample[i]):
                    isBreak = True
                    break
            if(isBreak):
                break
            else:
                result += 1
                
        return sample[:result]