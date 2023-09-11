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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == nullptr) return head;
        ListNode* result = head;
        while(head != nullptr && head->next != nullptr) {
            if(head->val != head->next->val) {
                head = head->next;
            } else {
                ListNode* next = head->next;
                while(next->next != nullptr && next->val == next->next->val) {
                    next = next->next;
                }
                head->next = next->next;
                head = head->next;
            }
        }
        return result;
    }
};