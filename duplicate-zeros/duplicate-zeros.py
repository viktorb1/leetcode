class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
         
        shift = arr.count(0)
        
        for i in range(len(arr)-1, -1, -1):
            if i + shift < len(arr):
                arr[i+shift] = arr[i]
            
            if arr[i] == 0:
                shift -= 1
                if i + shift < len(arr):
                    arr[i+shift] = 0