# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:12:50 2021

@author: user
https://leetcode.com/problems/subsets-ii/discuss/1380366/Java-or-Python-or-Recursion-Visualization
"""

# original
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        nums.sort()
        for num in nums:
            output += [curr + [num] for curr in output]
        
        final = []
        for element in output:
            
            if element not in final:
                final.append(element)

        return final