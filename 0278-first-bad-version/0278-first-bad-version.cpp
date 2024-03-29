// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int i = 1, j = n, m, bad;
        while(i <= j) {
            m = i + (j-i)/2;
            if(isBadVersion(m)) {
                bad = m;
                j = m-1;
            } else {
                i = m+1;
            }
        }
        return bad;
    }
};