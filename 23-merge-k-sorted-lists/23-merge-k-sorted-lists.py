# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
            
        start = ListNode(0)
        cur = start
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put(Wrapper(l))
            
        while not q.empty():
            node = q.get().node
            cur.next = node
            cur = cur.next
            
            if node.next:
                q.put(Wrapper(node.next))

        return start.next