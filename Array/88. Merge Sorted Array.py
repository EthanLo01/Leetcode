# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:15:58 2021

@author: user
"""

# https://leetcode.com/problems/merge-sorted-array/discuss/1437115/Very-efficient-and-Easy-to-understand-Python-solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            if m<=len(nums1):
                nums1[m]=i
                m+=1
        nums1.sort()
