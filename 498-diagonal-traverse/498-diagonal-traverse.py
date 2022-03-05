class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rows[i+j].append(mat[i][j])

        for i in rows:
            if i % 2 == 0:
                rows[i].reverse()
        
        return [j for i in rows.values() for j in i]