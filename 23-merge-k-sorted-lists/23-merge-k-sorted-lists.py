# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Wrapper:
            def __init__(self, node):
                self.node = node
                
            def __lt__(self, other):
                return self.node.val < other.node.val
            
        q = PriorityQueue()
        start = cur = ListNode(0)
        
        for l in lists:
            if l:
                q.put(Wrapper(l))
                
            
        while not q.empty():
            smallest = q.get().node
            cur.next = smallest
            cur = cur.next
            
            if smallest.next:
                q.put(Wrapper(smallest.next))
            
            
        return start.next