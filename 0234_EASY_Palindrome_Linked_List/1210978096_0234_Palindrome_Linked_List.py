# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev, cur = None, head
        count = 0

        while cur:
            setattr(cur, 'prev', prev)
            prev = cur
            cur = cur.next
            count += 1
        
        last = prev
        first = head
        
        for _ in range(count // 2):
            if last.val != first.val:
                return False
            
            last = last.prev
            first = first.next

        return True
