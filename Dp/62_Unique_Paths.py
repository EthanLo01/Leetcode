# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:47:20 2021

@author: user
"""

# https://leetcode.com/problems/unique-paths/discuss/1341105/simple-oror-easy-to-understand-oror-python
# God:
class Solution:
    def uniquePaths(self, m, n):

        dp = [[1 for i in range(0,m)] for j in range(0,n) ] 
        print(dp)
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[-1][-1]