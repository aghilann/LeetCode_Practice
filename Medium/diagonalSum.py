class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = {}
        row_len = len(mat) - 1
        col_len = len(mat[0]) - 1
        answer = []
        
        def primary(i, j):
            if i < 0 or j < 0 or i > row_len or j > col_len:
                pass
            else:
                visited[(i, j)] = True
                answer.append(mat[i][j])
                primary(i+1, j+1)
        
        def secondary(i, j):
            if visited.get((i, j)):
                secondary(i+1, j-1)
            elif i < 0 or j < 0 or i > row_len or j > col_len:
                pass
            else:
                answer.append(mat[i][j])
                secondary(i+1, j-1)
        
        primary(0, 0)
        secondary(0, len(mat[0]) - 1)
        
        return sum(answer)
