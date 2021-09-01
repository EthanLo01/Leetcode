# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:39:38 2021

@author: user

"""

# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/1421092/O(log(n))-time-or-O(1)-space
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            potential_match = nums[middle]
            left_num = nums[left]
            right_num = nums[right]
            if potential_match == target:
                return middle
            elif left_num <= potential_match:
                if target < potential_match and target >= left_num:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target > potential_match and target <= right_num:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1