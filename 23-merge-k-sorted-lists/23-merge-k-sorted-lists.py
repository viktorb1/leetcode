# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for l in lists:
            while l:
                ans.append(ListNode(l.val))
                l = l.next

        ans.sort(key=lambda x: x.val)
        for i, node in enumerate(ans[:-1]):
            node.next = ans[i+1]
        
        return ans[0] if len(ans) > 0 else None