# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:58:42 2021

@author: user
"""
#  https://leetcode.com/problems/unique-paths-ii/discuss/1422388/python-DP-solution
class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid[0]), len(grid)
        dp = [[0 for __ in range(m)] for _ in range(n)]
        
        n_1 = False
        for i in range(n):
            if grid[i][0] == 1:
                n_1 = True
            if not n_1 and grid[i][0] == 0:
                dp[i][0] = 1
        
        m_1 = False
        for j in range(m):
            if grid[0][j] == 1:
                m_1 = True
            if not m_1 and grid[0][j] == 0:
                dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
    

#  https://leetcode.com/problems/unique-paths-ii/discuss/1373117/Python-Clean-or-98.66-83.65
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not (obstacleGrid[0][0], obstacleGrid[-1][-1]) == (0, 0): return 0
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid = [[int(not obstacleGrid[r][c]) for c in range(N)] for r in range(M)]
        for c in range(1, N): 
            if obstacleGrid[0][c-1] == 0: obstacleGrid[0][c] = 0
        for r in range(1, M): 
            if obstacleGrid[r-1][0] == 0: obstacleGrid[r][0] = 0
        for r in range(1, M):
            for c in range(1, N):
                if obstacleGrid[r][c] == 1: 
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
        return obstacleGrid[-1][-1] 