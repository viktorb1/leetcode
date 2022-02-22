import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        vals = [i for i in count]
        
        
        def partition(vals, start, end, pivot):
            vals[pivot], vals[end] = vals[end], vals[pivot]
            
            dividor = start
            for i in range(start, end+1):
                if count[vals[i]] > count[vals[end]]:
                    vals[dividor], vals[i] = vals[i], vals[dividor]
                    dividor += 1
            
            vals[end], vals[dividor] = vals[dividor], vals[end]
            return dividor
        
        
        def quickselect(start, end):
            
            if start == end:
                return
            
            pivot = partition(vals, start, end, random.randint(start, end))
            
            if pivot == k:
                return
            elif pivot > k:
                quickselect(start, pivot - 1)
            elif pivot < k:
                quickselect(pivot + 1, end)
        
        
        quickselect(0, len(vals)-1)
        return vals[:k]
                