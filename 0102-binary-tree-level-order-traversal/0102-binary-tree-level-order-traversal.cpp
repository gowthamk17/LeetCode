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
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::queue<TreeNode*> level_queue;
        vector<vector<int>> levels;
        if(root != nullptr) {
            level_queue.push(root);
        }
        while(!level_queue.empty()) {
            int queue_len = level_queue.size();
            vector<int> level;
            while(queue_len) {
                TreeNode* node = level_queue.front();
                level_queue.pop();
                if(node != nullptr) {
                    level_queue.push(node->left);
                    level_queue.push(node->right);
                    level.push_back(node->val);
                }
                queue_len--;
            }
            if(!level.empty()) {
                levels.push_back(level);
            }
        }
        
        return levels;
    }
};