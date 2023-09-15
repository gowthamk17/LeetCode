/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return helper(nums, 0, nums.size()-1);
    }
    
    TreeNode* helper(vector<int>& nums,int l, int r) {
        if(l > r) {
            return nullptr;
        }
        int m = (l+r) / 2;
        TreeNode* root = new TreeNode(nums[m]);
        root->left = helper(nums, l, m-1);
        root->right = helper(nums, m+1, r);
        return root;
    }
};