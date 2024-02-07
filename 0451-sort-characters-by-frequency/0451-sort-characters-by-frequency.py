class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freq = {}
        for k, v in count.items():
            if v not in freq:
                freq[v] = [k]
            else:
                freq[v].append(k)
        
        ans = self.merge_sort(list(freq.items()))
        ans = [ y for (x, y) in ans]
        flat = [y*count[y] for x in ans for y in x]
        return ''.join(flat)
        
    
    def merge_sort(self, arr):
        if len(arr) > 1:
            q = (len(arr)+1) // 2
            l = self.merge_sort(arr[:q])
            r = self.merge_sort(arr[q:])
            return self.merge(l, r)
        
        return arr
    
    def merge(self, l, r):
        i, j = 0, 0
        ans = []
        
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                ans.append(l[i])
                i += 1
            else:
                ans.append(r[j])
                j += 1
        
        if i < len(l): ans += l[i:]
        if j < len(r): ans += r[j:]
        return ans