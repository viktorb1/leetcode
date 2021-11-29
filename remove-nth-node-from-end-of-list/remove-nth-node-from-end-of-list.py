# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        
        while curr:
            count += 1
            curr = curr.next
            
        remove = count - n
        count = 0
        curr = head
        prev = None
        
        while curr:
            count += 1
            if count == remove + 1:
                if prev:
                    prev.next = curr.next
                else:
                    head = head.next
                del curr
                break
            
            prev = curr
            curr = curr.next
            
        return head