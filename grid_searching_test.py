########### QUESTION ##############

# There are two grids where each cell of the grids contains either 0 or 1.
# If two cells share a side then they are adjacent. Cells that contain 1 form a connected region
# if any cell of that region can be reached by moving by row or column through the adjacent cells 
# that contain 1. Overlay the first grid onto the second and if a region of the first grid completely 
# matches a region of the second grid, the regions are matched. Count the total number of such matched 
# regions in the second grid.

def find_connected_regions(grid):
    def dfs(row, col, grid, visited, region):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0 or visited[row][col]:
            return
        visited[row][col] = True
        region.append((row, col))
        # Explore adjacent cells
        dfs(row - 1, col, grid, visited, region)
        dfs(row + 1, col, grid, visited, region)
        dfs(row, col - 1, grid, visited, region)
        dfs(row, col + 1, grid, visited, region)

    def get_regions(grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        regions = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    region = []
                    dfs(row, col, grid, visited, region)
                    regions.append(region)
        return regions

    return get_regions(grid)

# Implement a function to find connected regions using DFS or BFS.

def count_matched_regions(grid1, grid2):
    # Step 1: Identify connected regions in both grids
    regions1 = find_connected_regions(grid1)
    regions2 = find_connected_regions(grid2)

    def regions_match(region1, region2):
        return set(region1) == set(region2)
    
    # Step 3: Initialize a counter for matched regions
    matched_count = 0
    
    # Step 4: Compare regions from the first grid with the second grid
    for region1 in regions1:
        for region2 in regions2:
            if regions_match(region1, region2):
                matched_count += 1
    
    # Step 5: Return the count of matched regions
    return matched_count

# Example usage:
grid1 = [[1,1,1],[1,0,1],[1,0,0]]
grid2 = [[1,1,1],[1,0,0],[1,0,1]]
matched_regions = count_matched_regions(grid1, grid2)
print(matched_regions)