# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:46:32 2021

@author: user
"""
# Solution
class Solution:
    def subsets(self, nums):

        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output