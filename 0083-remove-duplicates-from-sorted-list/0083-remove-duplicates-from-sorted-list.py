# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        while head and head.next:
            if head.val != head.next.val:
                head = head.next
            else:
                second = head.next
                while second.next and second.val == second.next.val:
                    second = second.next
                head.next = second.next
                head = head.next               
        return result