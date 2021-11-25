from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.q = deque()
        self.size = 0
        self.capacity = capacity
    
    
    def get(self, key: int) -> int:
        if key in self.d:
            self.q.remove(self.d[key]) # bottleneck
            self.q.append(self.d[key])
            return self.d[key][1]
        
        return -1

    
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.q.remove(self.d[key])
            self.size -= 1
        
        if self.size >= self.capacity:
            x = self.q.popleft()
            del self.d[x[0]]
            self.size -= 1
        
        self.d[key] = [key, value]
        self.q.append(self.d[key])
        self.size += 1
          

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
