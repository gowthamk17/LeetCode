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
    ListNode* removeElements(ListNode* head, int val) {
        if(head == NULL) return head;
        while(head && head->val == val) {
            head = head->next;
        }
        ListNode* copyHead = head;
        while(head) {
            if(head->next && head->next->val == val) {
                ListNode* nextValid = head->next;
                while(nextValid->next && nextValid->next->val == val) {
                    nextValid = nextValid->next;
                }
                head->next = nextValid->next;
            }
            head = head->next;
        }
        return copyHead;
    }
};