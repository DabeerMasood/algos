class Solution(object):
    count = 0
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if(grid[i][j]) == 1:
                    return self.finder(grid, i, j)
        return 0
                
    def finder(self, grid, i, j):
        if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == 0):
            return 1
        else:
            if grid[i][j] == 1:
                grid[i][j] = -1
                return self.finder(grid, i+1, j)+self.finder(grid, i-1, j)+self.finder(grid, i, j-1)+self.finder(grid, i, j+1)
            else:
                return 0
