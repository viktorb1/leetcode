# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        new_head = head
        
        if not head or not head.next:
            return head
        
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        
        k = k % count
        
        for i in range(k):
            prev, cur = None, head
            
            while cur.next:
                prev = cur
                cur = cur.next
                    
            new_head = cur
            new_head.next = head
            head = new_head
            prev.next = None
    
        return new_head
        
        