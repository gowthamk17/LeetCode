class Solution {
public:
    int maxArea(vector<int>& height) {
        int j = height.size() - 1;
        int i = 0;
        int curr;
        int area;
        while(i < j) {
            curr = (j - i) * min(height[i], height[j]);
            area = max(area, curr);
            if(height[i] <= height[j]) {
                ++i;
            } else {
                --j;
            }
        }
        return area;
    }
};