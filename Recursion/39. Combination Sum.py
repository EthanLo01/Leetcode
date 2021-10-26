# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 18:51:56 2021

@author: user
"""
#  https://leetcode.com/problems/combination-sum/discuss/1366210/Python-simple-DFS-faster-than-95-with-explanation
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        can = candidates
        ans = []
        def explore(r, s, i):
            for j in range(i, n):
                total = s + can[j]
                if total==target:
                    t = r + [can[j]]
                    ans.append(t)
                elif total<target:
                    t = r + [can[j]]
                    explore(t, total, j)
        
        explore([], 0, 0)
        return ans  
                