# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ll = []
        ptr = head
        
        while ptr:
            ll.append(ptr)
            ptr = ptr.next
                
        for i in range(0, len(ll), k):
            for j in range(i, (i+i+k)//2):
                l = j
                r = i+k-(j-i)-1
                
                if r >= len(ll):
                    break
                
                ll[l], ll[r] = ll[r], ll[l]
        
        for x, y in zip(ll, ll[1:]):
            x.next = y
            y.next = None
        
        return ll[0]
                
