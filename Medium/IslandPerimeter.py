class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        visited = {}
        
        def dfs(i, j):
            if i >= row_len or j >= col_len or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            
            elif visited.get(f"({i}, {j})"):
                return 0
            
            else:
                visited[f"({i}, {j})"] = 1
                perimeter_sum = dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
                return perimeter_sum
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        
        # This question is a LeetCode Easy but people say it's a Medium so I will say it too
        # I was unable to come up with the solution myself and I was using the right approch
        # but moddeling the data wrong as this is my first ever Graph question.
        # I watched a YouTube video on how to solve it after I failed.
            
