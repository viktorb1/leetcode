class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat[0]) * len(mat) != r*c: return mat
        sol = []
        val = self.getNext(mat)
        
        for _ in range(r):
            sol.append([])
            for _ in range(c):
                sol[-1].append(next(val))
        
        return sol
        
    def getNext(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                yield mat[i][j]
        
        