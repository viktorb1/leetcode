# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        even = head
        odd = head.next
        save = odd
        
        while even.next and odd.next:
            even.next = even.next.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next
        
        even.next = save
        return head