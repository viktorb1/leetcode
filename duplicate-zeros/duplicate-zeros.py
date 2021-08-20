class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
         
        i = 0
        while i < len(arr):
            if arr[i] == 0 and i < len(arr) - 1:
                for j in range(len(arr)-1, i, -1):
                        arr[j] = arr[j-1]
                
                arr[i+1] = 0
                i += 1
            
            i += 1
                