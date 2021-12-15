class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.jumpTo(arr, start, set()) 
        
    def jumpTo(self, arr, i, seen):
        if i < 0 or i >= len(arr):
            return False
        elif arr[i] == 0:
            return True
        elif i in seen:
            return False
        
        seen.add(i)
        return self.jumpTo(arr, i + arr[i], seen) or self.jumpTo(arr, i - arr[i], seen)