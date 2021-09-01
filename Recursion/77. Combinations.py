# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:31:03 2021

@author: user
"""

# https://leetcode.com/problems/combinations/discuss/1351535/Python3-Backtracking-Simple
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        def backtrack(low,comb):
            if len(comb) == k:
                res.append(list(comb))
                return
            for i in range(low,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(1,[])
        return res
