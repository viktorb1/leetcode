import random

class RandomizedSet:

    def __init__(self):
        self.items = dict()
        self.mirror = []

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        else:
            self.items[val] = len(self.mirror)
            self.mirror.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        else:
            idx_to_del = self.items[val]
            val_to_rpc = self.mirror.pop()
            del self.items[val]
            if idx_to_del < len(self.mirror):
                self.mirror[idx_to_del] = val_to_rpc
                self.items[val_to_rpc] = idx_to_del
            return True

    def getRandom(self) -> int:
        x = random.randint(0, len(self.mirror)-1)
        return self.mirror[x]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()