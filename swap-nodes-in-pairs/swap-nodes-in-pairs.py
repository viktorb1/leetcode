# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr and curr.next:

            if prev:
                prev.next = curr.next
            else:
                head = curr.next
            
            save = curr.next.next
            curr.next.next = curr
            curr.next = save
            
            prev = curr
            curr = curr.next
        
        return head
