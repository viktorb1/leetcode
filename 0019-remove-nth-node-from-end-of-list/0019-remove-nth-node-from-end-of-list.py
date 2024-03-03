# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        prev, cur = None, head
        
        while cur:
            cur = cur.next
            count += 1
        
        count -= n
        cur = head
        while cur:
            if (count == 0): break
            prev = cur
            cur = cur.next
            count -= 1
        
        if prev:
            prev.next = cur.next if cur else None
        else:
            head = head.next
        
        return head