# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:49:03 2021

@author: user
"""
# original
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            
            first = nums[i]
            
            #sec round
            for j in range(i+1, len(nums)):
                sec = nums[j]
                
                sum_int = first+sec
                if sum_int == target:
                    return [i, j]

# https://leetcode.com/problems/two-sum/discuss/1432861/Python-Solution%3A
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in visited:
                return [visited[difference], index]
            else:
                visited[number] = index

        
                