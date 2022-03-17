# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev, cur = None, ListNode(0)
        cur.next = head
        
        while cur.next:
            nextnext = cur.next
            nextnextnext = nextnext.next
            cur.next = prev
            
            cur2 = cur
            while cur2.next and nextnext.val > cur2.next.val:
                cur2 = cur2.next
            
            cur2next = cur2.next #save value
            cur2.next = nextnext
            nextnext.next = cur2next
            
            prev = cur.next
            cur.next = nextnextnext
            
        return prev