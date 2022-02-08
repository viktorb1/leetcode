# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        cur = head
        
        while cur:
            l.append(cur)
            cur = cur.next
        
        n = len(l)
        for i in range(n//2):
            l[i].next = l[n-i-1]
            l[n-i-1].next = l[i+1]
            
        l[n//2].next = None
        return head