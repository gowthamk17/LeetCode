/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA = 0, lenB = 0;
        ListNode* dummyA = headA;
        ListNode* dummyB = headB;
        while(dummyA != nullptr) {
            lenA++;
            dummyA = dummyA->next;
        }
        while(dummyB != nullptr) {
            lenB++;
            dummyB = dummyB->next;
        }
        int diff = abs(lenA-lenB);
        if(lenA>lenB) {
            while(diff--){
                headA = headA->next;
            }
        } else {
            while(diff--){
                headB = headB->next;
            }
        }
        while(headA != nullptr && headB != nullptr) {
            if(headA == headB) return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
}; 