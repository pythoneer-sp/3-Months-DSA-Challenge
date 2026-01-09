"""
GFG: Rat in a Maze Problem
Consider a rat placed at position (0, 0) in an n x n square matrix mat[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:

0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.

Note: Return the final result vector in lexicographically smallest order.

Examples:

Input: mat[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.
"""



class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        n= len(maze)
        res = [] #store possible paths
        choices = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]  # Possible moves
        
        def isValid(x,y):
            return 0 <= x < n and 0<= y < n and maze[x][y]==1
            
            
        def solve(x,y,path):
            if x== n-1 and y==n-1:  #Base condition
                res.append(path)
                return
            
            maze[x][y]=0  # mark current cell as visited
            
            for dname, dx, dy in choices:
                new_x, new_y = x+dx , y+dy
                if isValid(new_x, new_y):
                    solve(new_x, new_y, path+dname) #recursive call
                    
            # Restore the original value i.e Backtracking
            maze[x][y]=1
            
        
        if maze[0][0]==1:
            solve(0,0,"")
            
        return res
            