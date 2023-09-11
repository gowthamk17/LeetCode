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
    vector<int> postorderTraversal(TreeNode* root) {
        if(root == nullptr) return vector<int>();
        vector<int> result;
        
        // left
        vector<int> left = postorderTraversal(root->left);
        result.insert(result.end(), left.begin(), left.end());

        // right
        vector<int> right = postorderTraversal(root->right);
        result.insert(result.end(), right.begin(), right.end());

        // value
        result.push_back(root->val);
        
        return result;
    }
};