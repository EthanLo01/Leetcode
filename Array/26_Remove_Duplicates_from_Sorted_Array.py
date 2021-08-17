# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:16:07 2021

@author: user
"""

# God:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
	nums.sort()
	index = 1
	for i in range(1,len(nums)):
	    if(nums[i-1]!=nums[i]):
		nums[index] = nums[i]
		index+=1
	return index



