class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range((len(board[0]))):
                if board[i][j] == 'R':
                    k,l = i-1,j-1
                    m,n = i+1,j+1
                    
                    while k > 0 and board[k][j] == '.':
                        k -= 1
                    
                    while l > 0 and board[i][l] == '.':
                        l -= 1
                    
                    while m < 7 and board[m][j] == '.':
                        m += 1
                    
                    while n < 7 and board[i][n] == '.':
                        n += 1
                    
                    potential_matches = (
                        board[k][j],
                        board[i][l],
                        board[m][j],
                        board[i][n]
                    )
                    
                    return sum(a == 'p' for a in potential_matches)