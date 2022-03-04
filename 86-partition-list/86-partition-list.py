# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        list1 = ListNode(0)
        list2 = ListNode(0)
        begin1 = list1
        begin2 = list2
        
        while cur:
            
            if cur.val < x:
                list1.next = cur
                list1 = list1.next
            else:
                list2.next = cur
                list2 = list2.next
            
            cur = cur.next
        
        list1.next = begin2.next
        list2.next = None
        return begin1.next