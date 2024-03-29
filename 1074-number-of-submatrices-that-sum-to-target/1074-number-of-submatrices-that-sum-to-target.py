class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        count = 0

        for sr in range(n):
            row = [0]*m

            for i in range(sr, n):
                row = [x + y for x, y in zip(matrix[i], row)]
                count += self.subarraySum(row, target)

        return count

    
# 560. solution
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        psum = 0
        psum_count = defaultdict(int)
        psum_count[0] = 1
        
        for n in nums:
            psum += n
            
            if psum - k in psum_count:
                count += psum_count[psum - k]
            
            psum_count[psum] += 1
        
        return count