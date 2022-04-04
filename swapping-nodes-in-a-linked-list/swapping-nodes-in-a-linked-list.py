# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth = None
        kthfromend = head
        end = head
        
        for _ in range(k-1):
            end = end.next
        
        kth = end
        end = end.next
        
        while end:
            kthfromend = kthfromend.next
            end = end.next
        
        kth.val, kthfromend.val = kthfromend.val, kth.val
        return head
        