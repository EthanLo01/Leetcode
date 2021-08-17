# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:12:48 2021

@author: user
"""

# original:

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_new = []
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums_new.append(nums[i])

            else:
                count += 1
        k = len(nums_new)
        for i in range(count):
            nums_new.append('_')
        return k

# god:

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                count += 1

        nums.sort()

        k = len(nums) - count

        return k


