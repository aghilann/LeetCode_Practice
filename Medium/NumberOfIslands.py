class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS Approch
        # When the Node called has a value of 0, you have reached water
        # Check every signle grid 
        # How to disgneiguse island from water
        # How to keep track of water
        
        visited = []
        count = 0
        
        def bfs(x, y): 
            
            if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
                pass
            elif (x, y) not in visited: # Not in visited, check this and kids
                if grid[x][y] == "0":
                    visited.append((x, y)) # Add the water node to visited
                elif grid[x][y] == "1":
                    visited.append((x, y))
                    bfs(x+1, y)
                    bfs(x-1, y)
                    bfs(x, y+1)
                    bfs(x, y-1)
        
        for x, row in enumerate(grid): # x is current index, row is Array
            for y, col in enumerate(row): # y is current index, col is "0" or "1"
                
                if (x, y) in visited or col == "0":
                    continue
                else:
                    count += 1
                    bfs(x, y)
                    
        return count  
                        
                    
