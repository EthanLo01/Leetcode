# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:33:09 2021

@author: user
"""
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/1410320/Easy-Understanding-Python-Olog(N)-Faster-Than-90-Python-Find-First-and-Last-Position
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=0
        e=len(nums)-1
        n=e
        lo=-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                lo=mid
                e=mid-1
            elif nums[mid]>target:
                e=mid-1
            else:
                s=mid+1
        s=0
        e=n


        up=-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]==target:
                up=mid
                s=mid+1
            elif nums[mid]>target:
                e=mid-1
            else:
                s=mid+1
        return [lo,up]# your code goes here