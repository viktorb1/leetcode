# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur = None, head
        diff = right - left + 1
        
        if not head or not head.next:
            return head
        
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            
        begin = cur
        before_begin = prev
        prev = None
        
        while diff:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
            diff -= 1
          
        begin.next = cur
        
        if before_begin:
            before_begin.next = prev
        else:
            head = prev
        
        return head
            
        