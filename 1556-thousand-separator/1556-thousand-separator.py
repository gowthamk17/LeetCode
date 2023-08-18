class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        else:
            s = str(n)
            s = s[::-1]
            slist = []
            for i in range(0,len(s), 3):
                slist.append(s[i:i+3])
            s = '.'.join(slist)[::-1]
            return s
            