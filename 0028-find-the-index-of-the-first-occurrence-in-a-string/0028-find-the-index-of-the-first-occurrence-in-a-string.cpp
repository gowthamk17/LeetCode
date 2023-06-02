class Solution {
public:
    int strStr(string haystack, string needle) {
        int nSize = needle.size();
        int hSize = haystack.size();
        if(nSize > hSize) return -1;
        if(nSize == hSize) {
            return (haystack == needle ? 0 : -1);
        }
        for(int i = 0; i <= hSize - nSize; i++) {
            string substr = haystack.substr(i, nSize);
            if(substr == needle) return i;
        }
        return -1;
    }
};