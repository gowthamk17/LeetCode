class Solution {
public:
    int thirdMax(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int N = nums.size();
        int idx= N-1, i, unique=0;
        while(idx>=0){
            unique++;
            i = idx-1;
            while(i>=0&&nums[i]==nums[idx]) i--;
            if(i == -1) return nums[N-1];
            idx=i;
            if(unique==2) return nums[idx];
        }
        return -1;
    }
};