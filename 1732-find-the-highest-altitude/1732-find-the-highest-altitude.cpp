class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int high_alt = 0;
        int cur_alt = 0;
        for(int alt: gain) {
            cur_alt += alt;
            high_alt = max(high_alt, cur_alt);
        }
        return high_alt;
    }
};