# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        
        if not head or not head.next:
            return head
        
        while cur:
            count += 1
            
            if not cur.next:
                cur.next = head
                break
            
            cur = cur.next
        
        k = k % count
            
        cur = head
        for _ in range(count-k-1):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        return new_head