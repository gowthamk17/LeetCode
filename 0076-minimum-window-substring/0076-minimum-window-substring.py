class Solution:
    def minWindow(self, s: str, t: str) -> str:
            if t == "":
                return ""
            countT, window = {}, {}
            for c in t:
                countT[c] = countT.get(c, 0) + 1
            have, need = 0, len(countT)
            left = 0
            result, result_len = [-1,-1], float("Infinity")
            for right in range(len(s)):
                c = s[right]
                window[c] = window.get(c, 0) + 1
                if c in countT and window[c] == countT[c]:
                    have += 1
                while have == need:
                    if (right - left + 1) < result_len:
                        result = [left, right]
                        result_len = right - left + 1
                    window[s[left]] -= 1
                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                    left += 1
            left, right = result
            return s[left: right+1] if result_len != float("Infinity") else ""