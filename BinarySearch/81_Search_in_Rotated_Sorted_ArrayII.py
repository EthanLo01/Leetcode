# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 09:18:49 2021

@author: user
"""
# original
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                return 1
            
        return False
    
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/1408906/90-python-3-line
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target not in nums:
            return False
        return True
    
    
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/1364861/idk-why-but-it-works-2-line-python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target in nums:
                return True