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
    vector<int> inorderTraversal(TreeNode* root) {
        if(root == nullptr) return vector<int>();
        
        vector<int> traversal;
        
        vector<int> leftTraversal = inorderTraversal(root->left);
        traversal.insert(traversal.end(), leftTraversal.begin(), leftTraversal.end());
        
        traversal.push_back(root->val);
        
        vector<int> rightTraversal = inorderTraversal(root->right);
        traversal.insert(traversal.end(), rightTraversal.begin(), rightTraversal.end());
        
        return traversal;
    }
};