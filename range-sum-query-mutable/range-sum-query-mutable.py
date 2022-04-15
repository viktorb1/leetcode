class Fenwick:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    
    def getSum(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s
    
    def addVal(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & (-idx)
    
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.prefixSums = Fenwick(len(nums))
        
        for i, v in enumerate(nums):
            self.prefixSums.addVal(i+1, v)

    def update(self, index, val):
        diff = val - self.nums[index]
        self.prefixSums.addVal(index+1, diff)
        self.nums[index] = val

    def sumRange(self, left, right):
        return self.prefixSums.getSum(right+1) - self.prefixSums.getSum(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)