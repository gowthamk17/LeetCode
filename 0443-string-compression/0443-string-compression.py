class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = ""
        c = chars[0]
        count = 0
        for i in range(len(chars)):
            if chars[i] == c:
                count += 1
            else:
                compressed += c
                if count > 1:
                    compressed += str(count)
                c = chars[i]
                count = 1
        compressed += c
        if count > 1:
            compressed += str(count)
        for i in range(len(compressed)):
            chars[i] = compressed[i]
        return len(compressed)
                