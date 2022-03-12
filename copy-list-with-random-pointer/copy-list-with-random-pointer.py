"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        cur_og = head
        cur_cp = save = Node(head.val)
        matches = {}
        
        while cur_cp:
            matches[cur_og] = cur_cp

            if cur_og.next:
                if cur_og.next not in matches:
                    cur_cp.next = Node(cur_og.next.val)         
                    matches[cur_og.next] = cur_cp.next
                else:
                    cur_cp.next = matches[cur_og.next]
            
            if cur_og.random:
                if cur_og.random not in matches:
                    cur_cp.random = Node(cur_og.random.val)
                    matches[cur_og.random] = cur_cp.random
                else:
                    cur_cp.random = matches[cur_og.random]
            
            cur_og = cur_og.next
            cur_cp = cur_cp.next
                
        return save
        