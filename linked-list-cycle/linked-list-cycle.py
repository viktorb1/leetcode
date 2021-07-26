# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr = head
        visited = {}
        
        while curr:
            if curr.val in visited and visited[curr.val] == curr.next:
                return True
            else:
                visited[curr.val] = curr.next
            
            if curr.next == None:
                return False
            
            curr = curr.next