# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow.next
        prev = None
        slow.next = None
        while cur:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        
        head1 = head
        head2 = prev
        while head1 and head2:
            save1 = head1.next
            save2 = head2.next
            head1.next = head2
            head1 = save1
            head2.next = head1
            head2 = save2
        
        
            