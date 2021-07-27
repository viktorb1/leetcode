# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        
        while curr:
            nex = curr.next
            
            if nex and curr.val == nex.val:
                curr.next = nex.next
                del nex
            else:
                curr = curr.next
        
        return head