/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        std::stack<int> stack;
        ListNode* dummy = head;
        while(dummy != NULL) {
            stack.push(dummy->val);
            dummy = dummy->next;
        }
        while(head != NULL) {
            if(head->val != stack.top()) {
                return false;
            }
            stack.pop();
            head = head->next;
        }
        return true;
    }
};