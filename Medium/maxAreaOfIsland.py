class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_island = 0
        visited = {}
        row_len = len(grid)
        col_len = len(grid[0])
        
        def dfs(x, y):
            
            if visited.get((x, y)):
                return 0    
            if (x < 0 or y < 0 or x > row_len - 1 or y > col_len - 1):
                return 0
            if grid[x][y] == 0:
                visited[(x, y)] = 0
                return 0
            if grid[x][y] == 1:
                visited[(x, y)] = 1
                return 1 + dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1)
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 1:
                    island_area = dfs(i, j)     
                    if island_area > max_island:
                        x = island_area - max_island
                        max_island += x
                    
                
        return max_island
