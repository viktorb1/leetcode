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
                
        ans = self.sortListNodes(ans)

        for i, node in enumerate(ans[:-1]):
            node.next = ans[i+1]
        
        return ans[0] if len(ans) > 0 else None
    
    def sortListNodes(self, ans):
        if len(ans) <= 1:
            return ans
        
        ans1 = self.sortListNodes(ans[:len(ans)//2])
        ans2 = self.sortListNodes(ans[len(ans)//2:])
        return self.combine(ans1, ans2)
            

    def combine(self, ans1, ans2):
        i, j = 0, 0
        sol = []

        while i < len(ans1) and j < len(ans2):
            if ans1[i].val < ans2[j].val:
                sol.append(ans1[i])
                i += 1
            else:
                sol.append(ans2[j])
                j += 1

        while i < len(ans1):
            sol.append(ans1[i])
            i += 1

        while j < len(ans2):
            sol.append(ans2[j])
            j += 1
        
        return sol