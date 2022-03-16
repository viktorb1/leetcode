# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left, right = left - 1, right - 1
        cur = head
        nodes = []
        
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        for k in range(left, (left+right+1)//2):
            nodes[k].val, nodes[right-(k-left)].val = nodes[right-(k-left)].val, nodes[k].val

        return head
            
        