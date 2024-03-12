# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        total = 0
        d = {0: dummy}
        
        while head: # calculate last item that sums to `n`
            total += head.val
            d[total] = head
            head = head.next
            
        head = dummy
        total = 0
        while head: # make first item that sums to `n` point to last item that sums to `n`
            total += head.val
            head.next = d[total].next
            head = head.next
        
        return dummy.next
            
        
        