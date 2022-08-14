class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1, i = digits.size()-1;
        while(carry){
            if(i >= 0){
                if(digits[i] == 9){
                    digits[i] = 0;
                }else{
                    digits[i]++;
                    carry = 0;
                }
            }else{
                digits.insert(digits.begin(),1);
                carry = 0;
            }
            i--;
        }
        return digits;
    }
};