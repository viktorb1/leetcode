class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def try_piece(arr):
            if not arr:
                return True
            
            for p in pieces:
                if p == arr[:len(p)]:
                    if try_piece(arr[len(p):]):
                        return True
                
            
            return False
                
            
        for p in pieces:
            if p == arr[:len(p)]:
                if try_piece(arr[len(p):]):
                    return True
            
            
        return False