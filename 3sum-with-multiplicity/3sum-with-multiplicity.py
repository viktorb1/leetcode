class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        count = 0
        
        for i in range(len(arr)-2):
            j = i + 1
            k = len(arr) - 1
            
            while j < k:
                total = arr[i] + arr[j] + arr[k]
                
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    l, r = 1, 1
                    while j+l < k and arr[j+l] == arr[j]: l += 1
                    while k-r >= j + l and arr[k-r] == arr[k]: r += 1
                    count += (l + r) * (l + r - 1) // 2 if arr[j] == arr[k] else l*r
                    j += l
                    k -= r
        
        return count % (10 ** 9 + 7)