class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int a = m+n-1, a1 = m-1, a2 = n-1;
        while(a2 >= 0){
            if(a1 >= 0 && nums1[a1] > nums2[a2]){
                nums1[a--] = nums1[a1--];
            }else{
                nums1[a--] = nums2[a2--];
            }
        }
          
    }
};