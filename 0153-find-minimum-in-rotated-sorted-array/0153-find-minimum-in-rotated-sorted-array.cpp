class Solution {
public:
    int findMin(vector<int>& nums) {
        int res = nums[0], left = 0, right = nums.size()-1, mid;
        while(left <= right)  {
            if(nums[left] < nums[right]) {
                res = min(res, nums[left]);
                break;
            }
            mid = left + (right - left) / 2;
            res = min(res, nums[mid]);
            if(nums[left] <= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
};