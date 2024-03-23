# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nodes = []

        while cur:
            nodes.append(cur)
            cur = cur.next
        
        n = len(nodes)
        for i in range(n//2):
            nodes[i].next = nodes[n-i-1]
            nodes[n-i-1].next = nodes[i+1]

        nodes[n//2].next = None
        return head