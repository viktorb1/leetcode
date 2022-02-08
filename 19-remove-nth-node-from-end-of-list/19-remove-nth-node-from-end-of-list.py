# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(node, count):
            if not node:
                return count[0]
            
            dfs(node.next, count)
            
            if count[0] == n:
                node.next = node.next.next
            
            count[0] += 1
            return count[0]
        
        x = dfs(head, [0])
        
        return head if n < x else head.next