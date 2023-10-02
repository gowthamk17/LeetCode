class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t rev = 0;
        int digit;
        for(int i = 0; i < 32; i++) {
            digit = n & 1;
            n >>= 1;
            rev <<= 1;
            rev |= digit;
        }
        return rev;
    }
};